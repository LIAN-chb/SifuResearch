# 玩家招式名称12：官网交叉核查

核查日：2026-10-29。此分支只查网页来源，不改招式图、生成器或现有命名。简体中文名称的权威对应由本批本地游戏本地化调查负责；以下不把攻略译名或代码变量当官方名称。

## 已核官网来源

### W01：2023-03-28官方更新说明

[Patch 1.19 / 1.20](https://www.sifugame.com/news/patch-1-19-1-20-arenas-day-1-patch)是Sloclap游戏官方网站发布的更新说明。其招式调整部分直接使用以下游戏英文名：

| 页面使用的名称 | 可支持的结论 |
|---|---|
| Duck Strike | 是官网正式使用的招式名 |
| Chasing Strikes | 是官网正式使用的招式名 |
| Invert Throw | 是官网正式使用的招式名 |
| Hook Intercept | 是官网正式使用的招式名 |
| Turnaround Duck Strike/Hook Intercept | 官方将转身版本与基础名称联系描述，不证明图中每个姿态资产有各自独立菜单名称 |
| Push Kick Combo | 官方以组合技名称描述相关调整，不宜默认它仅指组合中的某一击 |
| Chasing Trip Kick | 与前一个组合的后续动作一并被官方明确提及 |

定位：网页“Design Changes - Attacks/Moves”下各招式标题与推踢组合条目（本次web工具行113–143）。该页没有足以验证“追亡逐北”等简中对应的中文正文；不能仅凭此页完成中英映射。

### W02：2023-09-07官方最终内容更新

[Patch 1.24](https://www.sifugame.com/news/patch-1-24-the-final-content-update-is-out)在“Design”部分明确区分替换招式名与原本被替换的动作位置：Jump Punch替换位置由Running Light Attack改为Duck Strike；Bodyguard Grab替换位置由Crooked Foot改为Running Light Attack（本次工具行55–59）。这可证明菜单中还存在替换招式／招式组命名，不能把名称表无条件套到默认徒手树，也不能将动作位置标签与替换动作名视为同一件事。

### W03：范围与版本信息

[官方新闻索引](https://www.sifugame.com/news)指向上述两篇。另查[2022-05-03更新](https://www.sifugame.com/news/patch-1-08-spring-2022-content-update)及[2022-08-31更新](https://www.sifugame.com/news/patch-1-12-summer-content-update)，均无可用于完整核查简中招式对应的名称表。因此不再扩大为无差别攻略收集。

## 使用边界

本分支确认的是官网采用的英文拼写及名称所指层次。简中名称是否存在、与哪些操作对应，须由相同本地化namespace/key的中英文对照、实际技能／招式菜单文本引用或官方游戏画面补证；英文名与资源名近似不等于映射闭合。用户给出的“推击接重击＝追亡逐北”保留为待核样例，本分支未凭二手网页将它升级为官方证据。

初始宽泛搜索返回攻略、Wiki、论文和社区内容，仅作为候选线索；后续改为官网域名过滤并直接打开官方页。未将搜索摘要或社区动作解释作为正式名证据。结构化来源清单见`exports/20261029-玩家招式名称-12/web-sources.json`。

本分支写入结束；不需要用户操作，主批次继续以本机游戏文本完成简中对应核查。
