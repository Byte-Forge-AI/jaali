# Audio licenses

All audio is recorded/produced material released under **CC0 1.0 Universal (public domain dedication)**, https://creativecommons.org/publicdomain/zero/1.0/ . No attribution is required; credit is given anyway. Nothing is synthesised in code.

Processing done by us (ffmpeg): trim/loop-crossfade (music), mono down-mix, loudness normalisation, encode to Ogg Vorbis (q3) and MP3 fallback. Files are chosen at runtime with `canPlayType` (ogg, else mp3).

| File | Use | Original | Source URL | License | Provenance / evidence |
|---|---|---|---|---|---|
| music_loop.ogg / .mp3 | Background music loop (96 s, seamless 4 s crossfade, loudness-normalised) | "Calm Track" by pmiller (first 100 s of the 252 s track) | https://opengameart.org/content/calm-track | CC0 1.0 | Copy obtained from the GitHub mirror https://github.com/Andrew231716/visionai-music (commit c68a019, file audio/ambient/ambient_010.mp3, sha256 27e1d8f88e2f643ae499b35829059e81d62370e17880afd48646da0fc2d88f96). The mirror records license CC0-1.0 and the evidence "OpenGameArt page shows License(s): CC0, Public Domain, no attribution required" (metadata/license_manifest.json, entry calm_track). opengameart.org itself is blocked from this sandbox, so the OGA page could not be opened directly. |
| sfx_place.ogg / .mp3 | Place a pane | impact_glass_light_000 - Kenney "Impact Sounds" | https://kenney.nl/assets/impact-sounds | CC0 1.0 | GitHub port https://github.com/Boyquotes/kenney-impact-sounds-for-godot (commit 999dd16), repo LICENSE = CC0 1.0 legal text |
| sfx_gameover.ogg / .mp3 | Game over | impact_bell_heavy_002 - Kenney "Impact Sounds" | https://kenney.nl/assets/impact-sounds | CC0 1.0 | same as above |
| sfx_pick.ogg / .mp3 | Pick up a pane | select_003 - Kenney "Interface Sounds" | https://kenney.nl/assets/interface-sounds | CC0 1.0 | GitHub port https://github.com/Calinou/kenney-interface-sounds (commit 4596a49); pack LICENSE.txt states "License: (Creative Commons Zero, CC0)" |
| sfx_clear.ogg / .mp3 | Line clear | confirmation_002 - Kenney "Interface Sounds" | https://kenney.nl/assets/interface-sounds | CC0 1.0 | same as above |
| sfx_combo.ogg / .mp3 | Combo / multi-line (played at a rising playback rate for bigger combos) | confirmation_004 - Kenney "Interface Sounds" | https://kenney.nl/assets/interface-sounds | CC0 1.0 | same as above |
| sfx_click.ogg / .mp3 | Button click | click_001 - Kenney "Interface Sounds" | https://kenney.nl/assets/interface-sounds | CC0 1.0 | same as above |

## Copies of the license texts kept with the build

`licenses/` (in the build) and `audio/license_copies/` (in the project) contain:

- `kenney-interface-sounds_pack-LICENSE.txt` and `kenney-interface-sounds_LICENSE.txt` - Kenney Interface Sounds pack license (CC0) and the port repo license
- `kenney-impact-sounds_repo-LICENSE-CC0.txt` - CC0 1.0 legal text shipped in the Impact Sounds port repo
- `music-mirror_SOURCE_VERIFICATION.md` and `music-mirror_calm-track_manifest-entry.json` - the mirror's recorded verification for "Calm Track"

## Open points

- The music file is verified through a third-party mirror's records, not by opening the OpenGameArt page (blocked here). Before publishing, open https://opengameart.org/content/calm-track once and confirm it still shows License(s): CC0. If you want a zero-doubt alternative, swap `music_loop.*` for a Kenney-only track.
- Kenney's Impact Sounds port repo only ships the generic CC0 legal text, not Kenney's own pack readme; the pack is CC0 on https://kenney.nl/assets/impact-sounds.

## SHA-256 (first 16 hex) of shipped files

- music_loop.mp3 13b21f47ec925dfd 1152671 bytes
- music_loop.ogg ca407ce19853f091 794127 bytes
- sfx_clear.mp3 0790ae4ccd0cb1d1 5059 bytes
- sfx_clear.ogg 1c1caf20e271204c 6669 bytes
- sfx_click.mp3 5620d3da400e31fa 1506 bytes
- sfx_click.ogg eabfa27ccde8333a 4276 bytes
- sfx_combo.mp3 14d1f683478d3452 4641 bytes
- sfx_combo.ogg b9a45060f94505d3 5807 bytes
- sfx_gameover.mp3 8acd9d82e4a75768 6104 bytes
- sfx_gameover.ogg 6e32b7a0c463eea4 7782 bytes
- sfx_pick.mp3 40cd59cc260da8fc 3596 bytes
- sfx_pick.ogg 48fa9f2f07e523f3 6421 bytes
- sfx_place.mp3 9d94679109f602e4 2342 bytes
- sfx_place.ogg 019ff6d0fd1e7b5a 4840 bytes

## Primary-source check (2026-11-21)
- https://opengameart.org/content/calm-track opened in a browser: author pmiller, License: CC0.
- https://kenney.nl/assets/impact-sounds opened in a browser: License: Creative Commons CC0.
