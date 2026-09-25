# 🔒 VAULT V2 — LOCKED · V2 CLOSED

Locked on **2026-09-25**, after the final double red team (aesthetic + accuracy, see [`RED-TEAM.md`](RED-TEAM.md)).

**Rule: V2 CLOSED — no new render, re-mix or repackaging without Sami's explicit request.**

Nothing here is scheduled or published; the Buffer queue and the planned distribution were not touched. `engine/package.py` refuses to repackage a locked vault (override `BFYP_UNLOCK_V2=1`, only on that explicit request).

The 30 videos and 30 covers below were re-hashed on 2026-09-25 and match `manifest.json` (`python3 production/engine/lock_vault.py verify` re-checks them). File names carry the first 10 hex of their sha256.

| Reel | Video | sha256 (video) | sha256 (cover) | Red team |
|---|---|---|---|---|
| V2-01 | `V2-01_sec_hack-70e4d2b55a.mp4` | `70e4d2b55a7aa710a9b8d648180572fc39e8fa032f62b44ed39c6f5113b34433` | `1642fba06ec4b909c991338a6c4d7da67758036364d35f8a3d25a829e8c27de0` | PASS |
| V2-02 | `V2-02_gurus_100m-51aeb17b31.mp4` | `51aeb17b31c34a0f9ff7076e19753bffb4bd0e7a038397869af51f9235302c40` | `df207b781644429b80cb4d7f8bff97213003cf879e1f93281a6278d3a0e13ae5` | fixed (data) → re-check PASS |
| V2-03 | `V2-03_ai_fake_cases-f3104adee4.mp4` | `f3104adee49bda30cc9e1291fcf31228ded8e4661fb0f7ce3f855358387ab494` | `141eb8e6d2650e189a23cfb318e0fdd8081fdbb27cd48200412a5dd2d7f999e3` | PASS |
| V2-04 | `V2-04_fake_tweet-9cd795e4f5.mp4` | `9cd795e4f5597572e00476ffdc8fd874dfadefa13ec1b20f8e92b7a5925c471b` | `def5b94d9dbee912fc8cb7afb44b85c801b71aa7de735e74b64d658edddd84b1` | PASS |
| V2-05 | `V2-05_fake_reviews-1057fbe84c.mp4` | `1057fbe84cb9f0c4282a4e080ccb8ed93f6c0e8b7e07317f3c847b4b65fb439f` | `fef0d724f626f3cea295252a46a09a9fa0922e046109dc655e7d271547ad54aa` | PASS |
| V2-06 | `V2-06_feed_48-f2a31699ae.mp4` | `f2a31699aecf081ef7443af3192db7bbae7decbc087db3009cee957f2d80aa95` | `d6d52e6f51c5c2b86ba249f91a653012851fb9bdf78566b790e689c25001fda0` | PASS |
| V2-07 | `V2-07_just_bought-8b2e1509a8.mp4` | `8b2e1509a8a7b29a51af42f28364691483e990fb3e30d815acd4c664a7db2bba` | `bcaa852730034009d57e642442aad8301a5be34ff3212802455696dd4690745e` | PASS |
| V2-08 | `V2-08_trace_it-8463ea8b44.mp4` | `8463ea8b44a39f51ed9518efd8179799e73f2012c802b22c9c237f4822bd86cc` | `597976a729e030bb7d63b544c895c21965d63378e3fb7f344ad3c676c2202e27` | fixed (aesthetic) → re-check PASS |
| V2-09 | `V2-09_fiscal_2026-ba7b210971.mp4` | `ba7b210971f7c2ef449059c72e55ec3a5a3a42560bc4d12a0b11101635c47024` | `d742a5de3bae835d7c563cdd807c93c9adceb57de7009bec1b4fe9c99c3c373d` | PASS |
| V2-10 | `V2-10_top10_36-679f9df286.mp4` | `679f9df2865cf5d583c93be8f63f2de39451c7aebc950d50dbc65e8e2557741c` | `cdc6c772f0a02c59c833ddc2376293ec4dac1a527ed2b09e0649282c716c5036` | PASS |
| V2-11 | `V2-11_eleven_tabs-6d954d573c.mp4` | `6d954d573cf7dca1d036a07193bfb798df700f30aca78294e344c93c8ebea7c2` | `ee9419ff4ffb1f5ea5c6a5c74da1e88b9a31779f181650085320cabf636de7f6` | fixed (aesthetic) → re-check PASS |
| V2-12 | `V2-12_what_changed-c22f441447.mp4` | `c22f441447d937f9949c2e8f8cb13cb316556d5ef0319c6d1df3660050611543` | `81f83500b6bf09cb844d1f77f3984ec785c3bb7399dbfdde8236c970071accfc` | PASS |
| V2-13 | `V2-13_since_when-c98d824013.mp4` | `c98d82401344c4f2ab03d99c4cd47ef5f36633ea8b9472552df9fef70d8788f1` | `0491d6e3030a5dede9e404b3eaf5c919f9731263fd4fc94f62b71c921af6640b` | PASS |
| V2-14 | `V2-14_whale_alert-2a417572c6.mp4` | `2a417572c68b27d96f7789682761f68725d217ea03d3d45ee4722981c3b7ce2e` | `996496a3a3ff8004aa2c82b4d55488a4740e657d250fb8689ded7bebd77f23d3` | PASS |
| V2-15 | `V2-15_context_paste-07a26a4e61.mp4` | `07a26a4e614f039f3ed2d043d1bad53b49f0937ca6944e638718466c8492ceea` | `0dec48ac91d6a83db42c2ac71de06ef8684d347886351db4c7b33803dc583dc2` | fixed (data) → re-check PASS |
| V2-16 | `V2-16_cost_before-995bfb9067.mp4` | `995bfb9067975f0aa2aba1d9cf5e3e6d5db2a80da130bc81fa8428f91e496c7f` | `fa36e501ea446f3d5b00f5900470f98b04d557a37e0792d3d6053dce96878dae` | PASS |
| V2-17 | `V2-17_free_speedrun-4460acddce.mp4` | `4460acddceb354c22f4ef1ae4a66f5de2133a7c53d3d1831a9b24872b69e0c91` | `6478c0f226173249ef1a85d9fa1e8b1cebb1ecf99af4fcb6c14a1fafe93dccbf` | fixed (data) → re-check PASS |
| V2-18 | `V2-18_whose_trillion-88b7959b6b.mp4` | `88b7959b6bf1d3fed3d926bdae5f17dc1439369dcf7ec877b0173c13b99a79f5` | `5552c8f36375b15dcb7a634eecfe8f2f2f6efb5d123f5fb8b7f7ffe18fa83a49` | PASS |
| V2-19 | `V2-19_form_144-e994ca66f6.mp4` | `e994ca66f660ef798f7c5d945dc014250c2ebe29e02c85bdc9c0aa39da7f6b49` | `fbb0124981bb896bd5540ea2b9126be6f7d3b140d7813f50552a8a5a8c048c92` | fixed (aesthetic) → re-check PASS |
| V2-20 | `V2-20_financebench-76ac9a26de.mp4` | `76ac9a26de30a86414e7bf5e8d7d97ef693457dd0d8e80c1cb231ab462fe3680` | `38ff566a8d257246aaf2835e10bbdba575c7b4113604fae3c6cfe3551df732a7` | PASS |
| V2-21 | `V2-21_big_not_smart-cdcc185cb4.mp4` | `cdcc185cb4318b3ba40e6b769d6414822b040e69a8617799f8cacbe68b2b86f6` | `4a3f79198ca6a7a4d7e1f05f0e01b500f2fdfe94b0c5a1db65c6c8b6bc0a78de` | PASS |
| V2-22 | `V2-22_market_maker-c104a13bfb.mp4` | `c104a13bfb0e7b789bb480a77d6619d6a4fbc6789afb01a64b446ef68e2d2e64` | `bc47b9ca4c6993550c34de446dae4c67bac10a1a378ae200771c1a95847b7199` | fixed (data) → re-check PASS |
| V2-23 | `V2-23_same_score-0932e99823.mp4` | `0932e99823d09b4d3ca2bf34b7215f37b79e6e1585f68ee4a28bfd9bf1b25526` | `a54c4a3ee3cdddf12165281e89b8a96cf84ff14d80a92ed453f2762a8570fcab` | fixed (aesthetic) → re-check PASS |
| V2-24 | `V2-24_three_wins-894b1f220f.mp4` | `894b1f220fef445c1bd780df9cc7a619aea0fdd861f8b8bdecceeb9d2ff9b92b` | `58d984477e5d5885cc4a6df1ef2d03c1a239be1bac45948ff714a0f985ce83a8` | PASS |
| V2-25 | `V2-25_both_ways-eca9dd2b57.mp4` | `eca9dd2b573497422ef306a61517aa0fc7e8e56ca6145fb8ce9a3dbd321fac9d` | `c0bccaf1431e43d0112b36d6e627058c7c3ab01c8878ba188d1dfbd0d500559b` | PASS |
| V2-26 | `V2-26_together-c7bdbfa603.mp4` | `c7bdbfa603dcd93177b8f829a7aa21bea15a71c000614ecb9a936148ba1b698c` | `b51157caf0d96593ba2a0d37011c9c26f9accc10ff295d8151b32503fac7e758` | PASS |
| V2-27 | `V2-27_prove_it-2dbd45ce60.mp4` | `2dbd45ce600080dab1c2720603f69f1889a2de71a02094d3cd4c9b0d71696ff8` | `2b6ac9b45b1788f6f9411bedb0e7f69c2e804b5bdb969cdefc81b4d76d22a084` | PASS |
| V2-28 | `V2-28_no_invented-cc267ce528.mp4` | `cc267ce528b1b49adab3891bd90f790f491fde66710aa32b46986ecda8e28500` | `a343f8fe82313be7c80be4062f3c7f13209abc4b96f9733f17486c9a9f55972d` | PASS |
| V2-29 | `V2-29_timestamps-07942ec257.mp4` | `07942ec257e4097f40b7a7301a8e91d1ee7a5fd6542be1c28ce6d889bf5ec664` | `c9974d6b07d1a8ba151ef32b3d58511f819a05e94fc64ae92c2410f23f5f3b2a` | PASS |
| V2-30 | `V2-30_no_source-7611cfc534.mp4` | `7611cfc53455b966ce214231a36efd95627decb82f20bf233efdecde7c41295f` | `3206568be303dd2e0c175ce0c4e582253e1a3bfec6e28d582cf8a7fa1c5f4ed2` | fixed (aesthetic) → re-check PASS |

Sheets (`READY/*/V2-XX_slug.md`) are hashed in `manifest.json` (`sha256_sheet`).
