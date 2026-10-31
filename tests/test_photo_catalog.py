"""Keep the repository's browsable photo catalog synchronized with its source assets."""
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_catalog_matches_selection_and_assets() -> None:
	result = subprocess.run(
		[sys.executable, str(ROOT / 'devel/build_photo_catalog.py'), '--check'],
		cwd=ROOT, capture_output=True, text=True, check=False,
	)
	assert result.returncode == 0, result.stdout + result.stderr
	manifest = yaml.safe_load((ROOT / 'design_d_revised/data/photos.yml').read_text())
	records = yaml.safe_load((ROOT / 'docs/photos/inventory.yml').read_text())
	assert {record['id'] for record in records} == {photo['id'] for photo in manifest['photos']}
	assert {record['id'] for record in records if record['homepage']} == set(manifest['homepage_photos'])
	for record in records:
		assert record['full']['width'] >= record['thumbnail']['width']
		assert record['full']['height'] >= record['thumbnail']['height']

	train_hashes = [record.get('original', record['full'])['sha256'] for record in records if record['theme'] == 'trains']
	assert len(train_hashes) == len(set(train_hashes)), 'Train selection repeats the same photograph'
