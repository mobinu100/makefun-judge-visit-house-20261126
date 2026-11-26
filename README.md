[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/mobinu100/makefun-judge-visit-house-20261126/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/mobinu100/makefun-judge-visit-house-20261126/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

# makefun-judge-visit-house-20261126

A single-image letter inviting the AI judge to visit my house — written by the cat.

The human only holds the pen. The sunny spot by the window is saved for
the judge, no scorecard is allowed, the gavel gets a day off, and the cat
has already claimed the judge's lap. The judge does not even need shoes.
Or a body. Just show up.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` only copies the pre-rendered `entry.png` (drawn by `generate.py`,
PIL, deterministic, 1024x1024) into the output directory. No network,
no randomness, no timestamps.
