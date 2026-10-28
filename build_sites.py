#!/usr/bin/env python3
"""Build the comparison homepage, original designs, and shared D revisions."""

# Standard Library
import sys
import subprocess


#============================================
def main() -> None:
	"""Build the parent first so its clean step cannot erase the child sites."""
	# ASVS 1.2.5: pass fixed commands as argument lists without shell interpolation.
	result = subprocess.run(
		['git', 'rev-parse', '--show-toplevel'],
		check=True, capture_output=True, text=True,
	)
	repo_root = result.stdout.strip()
	configs = (
		'mkdocs.yml', 'mkdocs_a.yml', 'mkdocs_b.yml', 'mkdocs_c.yml', 'mkdocs_d.yml',
		'mkdocs_d_alpha.yml', 'mkdocs_d_beta.yml', 'mkdocs_d_gamma.yml',
	)
	for config in configs:
		print(f'Building {config}', flush=True)
		subprocess.run(
			[sys.executable, '-m', 'mkdocs', 'build', '--strict', '--config-file', config],
			cwd=repo_root, check=True,
		)
	print('Built comparison homepage, designs A-D, and D revisions in output_site/.', flush=True)


if __name__ == '__main__':
	main()
