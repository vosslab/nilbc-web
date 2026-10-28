# D revision wording review

The humanizer pass keeps the preferred slogan and specific club information.
D alpha, D beta, and D gamma use the same revised Markdown.

## Draft and final pass

Draft: "Our public shows welcome curious visitors of all ages. Bring the family."

Review: "curious visitors" adds little, and the invitation should explain whether membership
is required. The final copy keeps that practical distinction.

Final: "Our public shows welcome all ages. You do not need to be a member to visit."

## Changes from D

```diff
--- design_d/site_src/about/index.md
+++ design_d_revised/site_src/about/index.md
@@ -14,7 +14,7 @@
 builders. We give members a place to explore the hobby together and share their creations
 with the public.
 
-## A new name for a bigger table
+## Why we changed our name { #a-new-name-for-a-bigger-table }
 
 Since 2001 we have been the **Northern Illinois LEGO&reg; Train Club (NILTC)**. Our new
 name, **Northern Illinois Brick Club (NILBC)**, does two things:
@@ -22,15 +22,14 @@
 - **It removes a trademark from our name.** LEGO is a trademark of the LEGO Group. The club
   is not sponsored by the LEGO Group, and its name no longer suggests that it is.
 - **It says who we already are.** Members have always built far more than trains: town,
-  space, city, castle, Star Wars, Harry Potter, and more. A builder who has never laid
-  track should know right away that there is a seat for them.
+  space, city, castle, Star Wars, Harry Potter, and more. Builders who have never laid
+  track are welcome too.
 
 The trains are not going anywhere. They still run through almost every layout we bring to
 a show.
 
 The club also introduced a new identity: a round logo, a banner, and a mascot,
-[Matchstick](matchstick.md), a brick-built dragon who travels between every world members
-create.
+[Matchstick](matchstick.md), a brick-built dragon who can appear in any of our displays.
 
 While the change rolls out, you will still see the NILTC name on our email address and
 social media.
--- design_d/site_src/about/matchstick.md
+++ design_d_revised/site_src/about/matchstick.md
@@ -18,8 +18,8 @@
 
 ### :material-earth: He goes everywhere
 
-Our displays cover many themes. Matchstick ties them together, so one character can tell
-the story of a whole layout.
+Matchstick fits into many themes, so members can include him in different parts of a
+shared layout.
 
 ### :material-toy-brick-outline: He is fully buildable
 
@@ -41,8 +41,8 @@
 
 The color names and values below are a working digital reference, estimated from the
 rendered model shown here. They will be confirmed against the model's actual parts list.
-Lighting and reflections change how the rendering looks, so sample these values rather than
-the pictures.
+Lighting and reflections change the colors in the pictures. Use these values as provisional
+references until the parts list is confirmed.
 
 ///
 
--- design_d/site_src/index.md
+++ design_d_revised/site_src/index.md
@@ -10,17 +10,17 @@
 # the bar across the top of every page
 announcement:
   title: NILTC is now NILBC.
-  text: Same club, same trains, a bigger table for every kind of builder.
+  text: Our new name welcomes every kind of builder. The trains are staying.
   link_text: Why we changed our name
   link: about/#a-new-name-for-a-bigger-table
 ---
 
 /// hero | Northern Illinois Brick Club (formerly NILTC)
 
-# Every world, *brick by brick.*
+# Many interests. *One club.*
 
-We are adult builders from across northern Illinois. The trains still run, and the club now
-has room for castles, skylines, starships, creatures, and whatever you build next.
+We're adult LEGO builders from across northern Illinois. We build trains, castles,
+skylines, starships, creatures, and more.
 
 [See upcoming shows](shows/index.md){ .md-button .md-button--primary }
 [How to join](join/index.md){ .md-button }
@@ -39,24 +39,21 @@
 /// steps
 
 1. **Visit a show**
-   Most of our shows are in public libraries across the Chicago suburbs. Bring the family,
-   watch the trains run, and look closely for the tiny stories hidden in each scene.
+   All ages welcome. Watch the trains, explore the displays, and meet the builders.
+   No membership needed.
    [What to expect at a show](shows/visiting.md)
 2. **Explore the worlds**
-   Rail yards, skylines, landmarks, starships, castles, and creatures. See what members have
-   built and put on display.
+   See the trains, buildings, and characters our members create.
    [Browse member creations](creations/index.md)
 3. **Bring your builds**
-   Adults who love building in any theme are welcome. Email us, tell us what you build, and
-   come to a meeting.
+   Adult builders of every theme are welcome. Tell us what you like to build.
    [How membership works](join/index.md)
 
 ///
 
 ## Pick a world { data-kicker="Worlds we build" }
 
-Matchstick, our brick-built dragon, travels to every world members create. Where will you
-build?
+Explore the trains, buildings, and characters members bring to our shows.
 
 /// worlds
 
@@ -95,20 +92,15 @@
 
 /// split
 
-## Still a train club at heart { data-kicker="Trains included" }
+## Members make all kinds of things { data-kicker="Built by the club" }
 
-The club started in 2001 as the Northern Illinois LEGO&reg; Train Club. Trains are still
-the backbone of our layouts: Chicago commuter locomotives, freight lines, and steam engines
-running loops around everything else members bring.
+Members bring their own interests to our displays, from running trains to brick-built guitars.
 
-The table has always held more than trains: skyscrapers, castles, Paris at night, and a
-very happy Unikitty. Our new name, **Northern Illinois Brick Club**, finally says so.
-
-[Why we changed our name](about/index.md#a-new-name-for-a-bigger-table){ .md-button }
+[Get to know the club](about/index.md){ .md-button }
 
 ---
 
-![A long table display of brick-built houses, shops, trees, and a farm, with several parallel train tracks along the front edge.](assets/photos/library_layout.webp "A full show layout: village, farm, and several train lines.")
+![Club members behind large brick-built guitars, with a red pickup truck and other models on the table.](assets/photos/club_group_2026.webp "Yes, those are bricks.")
 
 ///
 
--- design_d/site_src/join/index.md
+++ design_d_revised/site_src/join/index.md
@@ -10,9 +10,8 @@
 
 # Join the club
 
-If you are an adult who builds, you are who we are looking for. Train builders, castle
-builders, city builders, sci-fi builders, and people who just want company while they
-build.
+We welcome adult builders with all kinds of interests. Tell us what you like to build
+and what you would like to do with the club.
 
 /// split
 
@@ -35,23 +34,22 @@
 
 ## How to join
 
-/// steps
+Email [niltc.contact@gmail.com](mailto:niltc.contact@gmail.com?subject=Membership) and include:
 
-1. **Email the club**
-   Write to [niltc.contact@gmail.com](mailto:niltc.contact@gmail.com?subject=Membership)
-   with your name, age, and where you live.
-2. **Show us what you build**
-   Tell us what you like to build and what you are working on now. Include links to photos
-   or videos of your builds.
-3. **Come to a meeting**
-   The club will invite you to a meeting to meet members and see what the club is like.
+- Your name
+- Your age
+- Where you live
+- What you like to build
+- Projects you are working on
+- Links to photos or videos of your builds
 
-///
+The club will invite you to a meeting to meet members and see what the club is like.
 
 /// callout | Before you write
 
 Age
-:   18 or older. NILBC is an adult club; families are welcome at every public show.
+:   18 or older. Families and other visitors of all ages are welcome at our public shows.
+    You do not need to join the club to attend.
 
 Getting there
 :   Reliable transportation to shows and meetings across northern Illinois.
@@ -70,7 +68,7 @@
 
 ## Not a train builder?
 
-You are exactly who the new name is for. Trains remain a big part of every layout, but the
+You are welcome here. Trains remain part of our displays, but the
 only theme rule for club displays is that builds are family friendly. Members build town,
 space, city, castle, Star Wars, Harry Potter, and more. Collaborative displays have their
 own [build standards](standards.md) so modules from different members line up.
--- design_d/site_src/shows/index.md
+++ design_d_revised/site_src/shows/index.md
@@ -30,8 +30,7 @@
 # Upcoming shows
 
 Come see the layouts in person. Our shows are hosted by public libraries and partner venues
-around the Chicago suburbs, and we bring trains, cities, and every other world members are
-building.
+around the Chicago suburbs. Members bring trains, cities, and other builds to share.
 
 Each host venue sets its own hours, parking, and policies, so check the venue's website
 before you travel.
@@ -41,8 +40,8 @@
 
 /// callout | Planning a visit?
 
-Read [what to expect at a show](visiting.md): how long to stay, what kids enjoy finding, and
-how to talk with builders. Curious where we have been? The [show logbook](logbook.md) lists
+Read [what to expect at a show](visiting.md) for tips on viewing the models, talking with
+builders, and checking admission and access. Curious where we have been? The [show logbook](logbook.md) lists
 our recent exhibitions.
 
 ///
--- design_d/site_src/shows/visiting.md
+++ design_d_revised/site_src/shows/visiting.md
@@ -11,8 +11,8 @@
 
 # Visiting a show
 
-A brick show is a museum where everything is built from the same small parts. Here is how
-to get the most out of it, whether you are five or fifty-five.
+Our public shows welcome visitors of all ages. You can walk around the displays, watch
+the trains, and talk with the people who built the models.
 
 /// steps
 
@@ -32,7 +32,7 @@
 
 /// cards
 
-### :material-hand-back-left-off-outline: Look with your eyes
+### :material-hand-back-left-off-outline: Please avoid touching the models
 
 Displays are built from thousands of loose parts and many are fragile. Please keep hands
 outside the barriers and help little ones do the same.
@@ -55,14 +55,14 @@
 
 ## Things to look for
 
-- **Running trains.** Most of our layouts use powered track running through scenery.
+- **Running trains.** Battery-powered trains run through the scenery on shared track.
   Builders follow shared [track and train standards](../join/standards.md) so modules from
   different members connect.
 - **Chicago in miniature.** Commuter locomotives, skylines, and local landmarks such as a
   replica of the DuPage County Historical Museum.
 - **Lights.** Some displays are wired with lights. A lit skyline or the Eiffel Tower
   glowing at dusk is worth staying for.
-- **Every other world.** Starships, cartoon towns, castles, and creatures. Ask the builder
+- **Other builds.** Starships, cartoon towns, castles, and creatures. Ask the builder
   which one they are proudest of.
 
 /// callout | From Matchstick
--- design_d/site_src/creations/index.md
+++ design_d_revised/site_src/creations/index.md
@@ -11,7 +11,7 @@
 
 # Worlds we build
 
-Every photo here shows real club work from past shows. Trains run through most of our
+Club builds and displays from the NILTC website archive. Trains run through most of our
 layouts, but members build whatever they love, as long as it is family friendly.
 
 /// world
```
