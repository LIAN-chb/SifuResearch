# Yang_ResistanceDB_Hard：受击与抗性配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB_Hard.uasset

这是资产自身保存的配置，不是每个引用者最终生效值；命中计数不能直接换算为拳数，普通硬直不套用眩晕计数。

## 反应限制对照

| 反应 | 累计伤害上限原值 | 累计命中上限原值 | 按攻击名合并 | 保留当前持续时间 | 持久标志 | 允许普通眩晕叠加 | 强制时长字段 | 时长字段 |
|---|---|---|---|---|---|---|---|---|
| 倒地 | -1.0 | 2 | False | True | False | 未保存 | 未保存 | 未保存 |
| 眩晕 | 40.0 | 2 | True | False | True | False | 未保存 | 未保存 |
| 推退 | 1.0 | -1 | True | False | False | 未保存 | 未保存 | 未保存 |
| 特殊眩晕 | -1.0 | -1 | 未保存 | 未保存 | 未保存 | 未保存 | 4.0 | 未保存 |
| 架势破坏 | 未保存 | 未保存 | 未保存 | 未保存 | True | 未保存 | 未保存 | 3.0 |

伤害上限 >0 才启用相应累计伤害退出检查；命中上限的更新与递增条件不完全相同。-1 等原值保留，具体解释见基础机制，不能把未保存字段补成 0。

## 按当前状态的抗性矩阵

| 状态 | 倒地抗性 | 推退抗性 | 眩晕抗性 | 自定义时长开关／值 | 使用受击动画时长 | 保留当前状态时长 | 保留阈值 | 自定义距离开关／值 |
|---|---|---|---|---|---|---|---|---|
| OutOfFight | 1 | 1 | 1 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| InFight | 5 | 6 | 2 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| Counter_Hit | 5 | 6 | 2 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| KnockedDown | 1 | 1 | 1 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| Dizzy | 0 | 0 | 0 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| Pushed | 1 | 10 | 15 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| Avoided | 1 | 1 | 1 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| StructureBroken | 1 | 1 | 1 | False / 0.0 | False | False | 1.0 | False / 0.0 |
| Parried | 1 | 1 | 1 | False / 0.0 | False | False | 1.0 | False / 0.0 |


## 本资产全部已解析保存字段

包含前表未展开的恢复动作、条件、图引用和其他字段。对象索引若尚未解析，不把索引当数值参数。

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[0].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[0].m_Level[1] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[0].m_Level[2] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[0].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[0].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[0].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[0].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[0].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[0].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[0] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[0].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[1].m_Level[0] | 5 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[1].m_Level[1] | 6 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[1].m_Level[2] | 2 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[1].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[1].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[1].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[1].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[1].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[1].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[1] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[1].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[2].m_Level[0] | 5 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[2].m_Level[1] | 6 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[2].m_Level[2] | 2 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[2].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[2].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[2].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[2].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[2].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[2].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[2] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[2].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[3].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[3].m_Level[1] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[3].m_Level[2] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[3].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[3].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[3].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[3].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[3].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[3].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[3] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[3].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[4].m_Level[0] | 0 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[4].m_Level[1] | 0 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[4].m_Level[2] | 0 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[4].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[4].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[4].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[4].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[4].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[4].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[4] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[4].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[5].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[5].m_Level[1] | 10 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[5].m_Level[2] | 15 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[5].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[5].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[5].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[5].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[5].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[5].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[5] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[5].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[6].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[6].m_Level[1] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[6].m_Level[2] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[6].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[6].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[6].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[6].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[6].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[6].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[6] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[6].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[7].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[7].m_Level[1] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[7].m_Level[2] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[7].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[7].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[7].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[7].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[7].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[7].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[7] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[7].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 特殊反应等级分量[0] | m_ResistanceMatrix[0].m_Matrix[8].m_Level[0] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 特殊反应等级分量[1] | m_ResistanceMatrix[0].m_Matrix[8].m_Level[1] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 特殊反应等级分量[2] | m_ResistanceMatrix[0].m_Matrix[8].m_Level[2] | 1 | 在攻击属性等级中分量 0／1／2 对应倒地／推退／眩晕；具体路径仍看状态与开关。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 启用自定义持续时间[0] | m_ResistanceMatrix[0].m_Matrix[8].m_bUseCustomDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 自定义持续时间值[0] | m_ResistanceMatrix[0].m_Matrix[8].m_fCustomDuration[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 使用受击动画时长[0] | m_ResistanceMatrix[0].m_Matrix[8].m_bUseHitAnimDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 保留当前状态剩余时长[0] | m_ResistanceMatrix[0].m_Matrix[8].m_bKeepCurrentStateDuration[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 保留当前状态时长阈值[0] | m_ResistanceMatrix[0].m_Matrix[8].m_fKeepCurrentStateThresold[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 启用自定义距离[0] | m_ResistanceMatrix[0].m_Matrix[8].m_bUseCustomDistance[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ResistanceMatrix）[0] → 未核中文义（m_Matrix）[8] → 自定义距离值[0] | m_ResistanceMatrix[0].m_Matrix[8].m_fCustomDistance[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_bIsConsidereredAsKnockdownThreat）[0] | m_bIsConsidereredAsKnockdownThreat[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInterruptDownWhenAlone）[0] | m_bInterruptDownWhenAlone[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_StateMoveDynamic）[0] | m_DownReaction[0].m_Movement[0].m_StateMoveDynamic[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fStateDistance）[0] | m_DownReaction[0].m_Movement[0].m_fStateDistance[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fDuration）[0] | m_DownReaction[0].m_Movement[0].m_fDuration[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_animation）[0] | m_DownReaction[0].m_RecoveryAnims[0].m_animation[0] | /Game/Animations/MainChar/OTG/Man/Dodge/MC_man_barehands_knockDown_dodge_south.MC_man_barehands_knockDown_dodge_south | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bMirror）[0] | m_DownReaction[0].m_RecoveryAnims[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bLoopable）[0] | m_DownReaction[0].m_RecoveryAnims[0].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fStartRatio）[0] | m_DownReaction[0].m_RecoveryAnims[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fPlayRate）[0] | m_DownReaction[0].m_RecoveryAnims[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_animation）[0] | m_DownReaction[0].m_RecoveryAnims[1].m_animation[0] | /Game/Animations/MainChar/OTG/Man/Dodge/MC_man_barehands_knockDown_dodge_south.MC_man_barehands_knockDown_dodge_south | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bMirror）[0] | m_DownReaction[0].m_RecoveryAnims[1].m_bMirror[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bLoopable）[0] | m_DownReaction[0].m_RecoveryAnims[1].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fStartRatio）[0] | m_DownReaction[0].m_RecoveryAnims[1].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fPlayRate）[0] | m_DownReaction[0].m_RecoveryAnims[1].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_animation）[0] | m_DownReaction[0].m_RecoveryAnims[2].m_animation[0] | /Game/Animations/MainChar/OTG/Man/Dodge/MC_man_barehands_knockDown_dodge_south.MC_man_barehands_knockDown_dodge_south | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bMirror）[0] | m_DownReaction[0].m_RecoveryAnims[2].m_bMirror[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bLoopable）[0] | m_DownReaction[0].m_RecoveryAnims[2].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fStartRatio）[0] | m_DownReaction[0].m_RecoveryAnims[2].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fPlayRate）[0] | m_DownReaction[0].m_RecoveryAnims[2].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_animation）[0] | m_DownReaction[0].m_RecoveryAnims[3].m_animation[0] | /Game/Animations/MainChar/OTG/Man/Dodge/MC_man_barehands_knockDown_dodge_south.MC_man_barehands_knockDown_dodge_south | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bMirror）[0] | m_DownReaction[0].m_RecoveryAnims[3].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bLoopable）[0] | m_DownReaction[0].m_RecoveryAnims[3].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fStartRatio）[0] | m_DownReaction[0].m_RecoveryAnims[3].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fPlayRate）[0] | m_DownReaction[0].m_RecoveryAnims[3].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bUseRootMotion）[0] | m_DownReaction[0].m_bUseRootMotion[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedDuration）[0] | m_DownReaction[0].m_HitReaction[0].m_fHittedDuration[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_HittedDynamic）[0] | m_DownReaction[0].m_HitReaction[0].m_HittedDynamic[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedKnockBackDistance）[0] | m_DownReaction[0].m_HitReaction[0].m_fHittedKnockBackDistance[0] | 100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedToStateBlendDuration）[0] | m_DownReaction[0].m_HitReaction[0].m_fHittedToStateBlendDuration[0] | 0.200000003 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bAlwayKeepCurrentStateDurationOnHit）[0] | m_DownReaction[0].m_bAlwayKeepCurrentStateDurationOnHit[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bPauseGuardBreak）[0] | m_DownReaction[0].m_bPauseGuardBreak[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bHoldDuringStructureBroken）[0] | m_DownReaction[0].m_bHoldDuringStructureBroken[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_fMaxAccumulatedDamage）[0] | m_DownReaction[0].m_fMaxAccumulatedDamage[0] | -1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_iMaxAccumatedHits）[0] | m_DownReaction[0].m_iMaxAccumatedHits[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bGroupMaxAccumulatedHitsByAttack）[0] | m_DownReaction[0].m_bGroupMaxAccumulatedHitsByAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnTick）[0] | m_DownReaction[0].m_Actions[0].m_OnTick[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnEnd）[0] | m_DownReaction[0].m_Actions[0].m_OnEnd[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_bIsPersistent）[0] | m_DownReaction[0].m_bIsPersistent[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_iPersistencePriority）[0] | m_DownReaction[0].m_iPersistencePriority[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DownReaction）[0] → 未核中文义（m_SuperAvailabilityLayer）[0] | m_DownReaction[0].m_SuperAvailabilityLayer[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_fDuration）[0] | m_StructureBrokenReaction[0].m_fDuration[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_animation）[0] | m_StructureBrokenReaction[0].m_Loop[0].m_animation[0] | /Game/Animations/Grunt/StructureBrokenState/Grunt_StructureBroken_loop.Grunt_StructureBroken_loop | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bMirror）[0] | m_StructureBrokenReaction[0].m_Loop[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bLoopable）[0] | m_StructureBrokenReaction[0].m_Loop[0].m_bLoopable[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fStartRatio）[0] | m_StructureBrokenReaction[0].m_Loop[0].m_fStartRatio[0] | 0.300000012 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fPlayRate）[0] | m_StructureBrokenReaction[0].m_Loop[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_bMirrorableLoop）[0] | m_StructureBrokenReaction[0].m_bMirrorableLoop[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_fGuardCoefRecoveredAtEnd）[0] | m_StructureBrokenReaction[0].m_fGuardCoefRecoveredAtEnd[0] | 0.300000012 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_fGuardRecoveredAtEnd）[0] | m_StructureBrokenReaction[0].m_fGuardRecoveredAtEnd[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_bIsPersistent）[0] | m_StructureBrokenReaction[0].m_bIsPersistent[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_iPersistencePriority）[0] | m_StructureBrokenReaction[0].m_iPersistencePriority[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_StructureBrokenReaction）[0] → 未核中文义（m_SuperAvailabilityLayer）[0] | m_StructureBrokenReaction[0].m_SuperAvailabilityLayer[0] | /Game/DB/Inputs/Availability/LayerData/GenericNone.GenericNone | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_animation）[0] | m_DizzyReaction[0].m_Loop[0].m_animation[0] | /Game/Animations/Grunt/DizzyState/Loop/Barehands/Grunt_barehands_dizzy_loop_head.Grunt_barehands_dizzy_loop_head | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bMirror）[0] | m_DizzyReaction[0].m_Loop[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bLoopable）[0] | m_DizzyReaction[0].m_Loop[0].m_bLoopable[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fStartRatio）[0] | m_DizzyReaction[0].m_Loop[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fPlayRate）[0] | m_DizzyReaction[0].m_Loop[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bMirrorableLoop）[0] | m_DizzyReaction[0].m_bMirrorableLoop[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bAllowDizzyOnTopOfDizzy）[0] | m_DizzyReaction[0].m_bAllowDizzyOnTopOfDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_StateMoveDynamic）[0] | m_DizzyReaction[0].m_Movement[0].m_StateMoveDynamic[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fStateDistance）[0] | m_DizzyReaction[0].m_Movement[0].m_fStateDistance[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fDuration）[0] | m_DizzyReaction[0].m_Movement[0].m_fDuration[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_animation）[0] | m_DizzyReaction[0].m_RecoveryAnims[0].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bMirror）[0] | m_DizzyReaction[0].m_RecoveryAnims[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bLoopable）[0] | m_DizzyReaction[0].m_RecoveryAnims[0].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fStartRatio）[0] | m_DizzyReaction[0].m_RecoveryAnims[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fPlayRate）[0] | m_DizzyReaction[0].m_RecoveryAnims[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_animation）[0] | m_DizzyReaction[0].m_RecoveryAnims[1].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bMirror）[0] | m_DizzyReaction[0].m_RecoveryAnims[1].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bLoopable）[0] | m_DizzyReaction[0].m_RecoveryAnims[1].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fStartRatio）[0] | m_DizzyReaction[0].m_RecoveryAnims[1].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fPlayRate）[0] | m_DizzyReaction[0].m_RecoveryAnims[1].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_animation）[0] | m_DizzyReaction[0].m_RecoveryAnims[2].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bMirror）[0] | m_DizzyReaction[0].m_RecoveryAnims[2].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bLoopable）[0] | m_DizzyReaction[0].m_RecoveryAnims[2].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fStartRatio）[0] | m_DizzyReaction[0].m_RecoveryAnims[2].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fPlayRate）[0] | m_DizzyReaction[0].m_RecoveryAnims[2].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_animation）[0] | m_DizzyReaction[0].m_RecoveryAnims[3].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bMirror）[0] | m_DizzyReaction[0].m_RecoveryAnims[3].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bLoopable）[0] | m_DizzyReaction[0].m_RecoveryAnims[3].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fStartRatio）[0] | m_DizzyReaction[0].m_RecoveryAnims[3].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fPlayRate）[0] | m_DizzyReaction[0].m_RecoveryAnims[3].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bUseRootMotion）[0] | m_DizzyReaction[0].m_bUseRootMotion[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedDuration）[0] | m_DizzyReaction[0].m_HitReaction[0].m_fHittedDuration[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_HittedDynamic）[0] | m_DizzyReaction[0].m_HitReaction[0].m_HittedDynamic[0] | /Game/DB/Hit/KnockBackDynamic.KnockBackDynamic | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedKnockBackDistance）[0] | m_DizzyReaction[0].m_HitReaction[0].m_fHittedKnockBackDistance[0] | 100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedToStateBlendDuration）[0] | m_DizzyReaction[0].m_HitReaction[0].m_fHittedToStateBlendDuration[0] | 0.100000001 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bAlwayKeepCurrentStateDurationOnHit）[0] | m_DizzyReaction[0].m_bAlwayKeepCurrentStateDurationOnHit[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bPauseGuardBreak）[0] | m_DizzyReaction[0].m_bPauseGuardBreak[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bHoldDuringStructureBroken）[0] | m_DizzyReaction[0].m_bHoldDuringStructureBroken[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_fMaxAccumulatedDamage）[0] | m_DizzyReaction[0].m_fMaxAccumulatedDamage[0] | 40 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_iMaxAccumatedHits）[0] | m_DizzyReaction[0].m_iMaxAccumatedHits[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bGroupMaxAccumulatedHitsByAttack）[0] | m_DizzyReaction[0].m_bGroupMaxAccumulatedHitsByAttack[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnTick）[0] | m_DizzyReaction[0].m_Actions[0].m_OnTick[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnEnd）[0] | m_DizzyReaction[0].m_Actions[0].m_OnEnd[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_bIsPersistent）[0] | m_DizzyReaction[0].m_bIsPersistent[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_iPersistencePriority）[0] | m_DizzyReaction[0].m_iPersistencePriority[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_DizzyReaction）[0] → 未核中文义（m_SuperAvailabilityLayer）[0] | m_DizzyReaction[0].m_SuperAvailabilityLayer[0] | /Game/DB/Inputs/Availability/LayerData/GenericNone.GenericNone | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyReaction）[0] → 未核中文义（m_fMandatoryDuration）[0] | m_SuperDizzyReaction[0].m_fMandatoryDuration[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyReaction）[0] → 未核中文义（m_fMaxAccumulatedDamage）[0] | m_SuperDizzyReaction[0].m_fMaxAccumulatedDamage[0] | -1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyReaction）[0] → 未核中文义（m_iMaxAccumatedHits）[0] | m_SuperDizzyReaction[0].m_iMaxAccumatedHits[0] | -1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 激活条件[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashHit[0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 激活条件[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashHit[0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 附加元数据[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashHit[0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 附加元数据[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashHit[0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 攻击效果行引用[0] → 数据表引用[0] | m_PushedReaction[0].m_WallSplashHit[0].m_HitRow[0].DataTable[0] | /Game/DB/_Shared/HitBox/Generic_HitBoxData.Generic_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 攻击效果行引用[0] → 数据行名称[0] | m_PushedReaction[0].m_WallSplashHit[0].m_HitRow[0].RowName[0] | WallSplashFar_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashHit[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashHit[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashHit[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashHit[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 命中检测配置[0] | m_PushedReaction[0].m_WallSplashHit[0].m_HitDetectionDB[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 命中部位类别[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 备用命中部位类别[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 瞄准目标类型[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 攻击运动类型[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → 攻击来源方向[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → Avoid 自定义来源方向[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → Avoid 自定义命中部位[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHit）[0] → Avoid 自定义动作类型[0] | m_PushedReaction[0].m_WallSplashHit[0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 激活条件[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 激活条件[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 附加元数据[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 附加元数据[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 攻击效果行引用[0] → 数据表引用[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_HitRow[0].DataTable[0] | /Game/DB/_Shared/HitBox/Generic_HitBoxData.Generic_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 攻击效果行引用[0] → 数据行名称[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_HitRow[0].RowName[0] | WallSplashClose_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 命中检测配置[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_HitDetectionDB[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 命中部位类别[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 备用命中部位类别[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 瞄准目标类型[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 攻击运动类型[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → 攻击来源方向[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → Avoid 自定义来源方向[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → Avoid 自定义命中部位[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashCloseHit）[0] → Avoid 自定义动作类型[0] | m_PushedReaction[0].m_WallSplashCloseHit[0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 激活条件[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 激活条件[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 附加元数据[0] → 类默认对象[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 附加元数据[0] → 条件或对象实例[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 攻击效果行引用[0] → 数据表引用[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_HitRow[0].DataTable[0] | /Game/DB/_Shared/HitBox/Generic_HitBoxData.Generic_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 攻击效果行引用[0] → 数据行名称[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_HitRow[0].RowName[0] | WallSplashOnEnvironment_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 命中检测配置[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/TakedownEnvImpactSphere.TakedownEnvImpactSphere | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 命中部位类别[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 备用命中部位类别[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 瞄准目标类型[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 攻击运动类型[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → 攻击来源方向[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → Avoid 自定义来源方向[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → Avoid 自定义命中部位[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_WallSplashHitOnWall）[0] → Avoid 自定义动作类型[0] | m_PushedReaction[0].m_WallSplashHitOnWall[0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 激活条件[0] → 类默认对象[0] | m_PushedReaction[0].m_HitBox[0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 激活条件[0] → 条件或对象实例[0] | m_PushedReaction[0].m_HitBox[0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 附加元数据[0] → 类默认对象[0] | m_PushedReaction[0].m_HitBox[0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 附加元数据[0] → 条件或对象实例[0] | m_PushedReaction[0].m_HitBox[0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 攻击效果行引用[0] → 数据表引用[0] | m_PushedReaction[0].m_HitBox[0].m_HitRow[0].DataTable[0] | /Game/DB/_Shared/HitBox/Generic_HitBoxData.Generic_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 攻击效果行引用[0] → 数据行名称[0] | m_PushedReaction[0].m_HitBox[0].m_HitRow[0].RowName[0] | PushedChara_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_PushedReaction[0].m_HitBox[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_PushedReaction[0].m_HitBox[0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_PushedReaction[0].m_HitBox[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_PushedReaction[0].m_HitBox[0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 命中检测配置[0] | m_PushedReaction[0].m_HitBox[0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/PushCharacter.PushCharacter | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 命中部位类别[0] | m_PushedReaction[0].m_HitBox[0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 备用命中部位类别[0] | m_PushedReaction[0].m_HitBox[0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 瞄准目标类型[0] | m_PushedReaction[0].m_HitBox[0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 攻击运动类型[0] | m_PushedReaction[0].m_HitBox[0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → 攻击来源方向[0] | m_PushedReaction[0].m_HitBox[0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → Avoid 自定义来源方向[0] | m_PushedReaction[0].m_HitBox[0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → Avoid 自定义命中部位[0] | m_PushedReaction[0].m_HitBox[0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_HitBox）[0] → Avoid 自定义动作类型[0] | m_PushedReaction[0].m_HitBox[0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_StateMoveDynamic）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_Movement[0].m_StateMoveDynamic[0] | /Game/DB/Hit/PushedDynamic.PushedDynamic | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fStateDistance）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_Movement[0].m_fStateDistance[0] | 500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fDuration）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_Movement[0].m_fDuration[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_animation）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[0].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bMirror）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_bLoopable）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[0].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fStartRatio）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[0] → 未核中文义（m_fPlayRate）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_animation）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[1].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bMirror）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[1].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_bLoopable）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[1].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fStartRatio）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[1].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[1] → 未核中文义（m_fPlayRate）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[1].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_animation）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[2].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bMirror）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[2].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_bLoopable）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[2].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fStartRatio）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[2].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[2] → 未核中文义（m_fPlayRate）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[2].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_animation）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[3].m_animation[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bMirror）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[3].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_bLoopable）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[3].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fStartRatio）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[3].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_RecoveryAnims）[3] → 未核中文义（m_fPlayRate）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_RecoveryAnims[3].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bUseRootMotion）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bUseRootMotion[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedDuration）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_HitReaction[0].m_fHittedDuration[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_HittedDynamic）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_HitReaction[0].m_HittedDynamic[0] | /Game/DB/_Shared/HitDynamic/PushedKnockBackDynamic.PushedKnockBackDynamic | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedKnockBackDistance）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_HitReaction[0].m_fHittedKnockBackDistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_HitReaction）[0] → 未核中文义（m_fHittedToStateBlendDuration）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_HitReaction[0].m_fHittedToStateBlendDuration[0] | 0.0799999982 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bAlwayKeepCurrentStateDurationOnHit）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bAlwayKeepCurrentStateDurationOnHit[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bPauseGuardBreak）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bPauseGuardBreak[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bHoldDuringStructureBroken）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bHoldDuringStructureBroken[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_fMaxAccumulatedDamage）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_fMaxAccumulatedDamage[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_iMaxAccumatedHits）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_iMaxAccumatedHits[0] | -1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bGroupMaxAccumulatedHitsByAttack）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bGroupMaxAccumulatedHitsByAttack[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnTick）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_Actions[0].m_OnTick[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_Actions）[0] → 未核中文义（m_OnEnd）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_Actions[0].m_OnEnd[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_bIsPersistent）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_bIsPersistent[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_iPersistencePriority）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_iPersistencePriority[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_BasePushReaction）[0] → 未核中文义（m_SuperAvailabilityLayer）[0] | m_PushedReaction[0].m_BasePushReaction[0].m_SuperAvailabilityLayer[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_animation）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Loop[0].m_animation[0] | /Game/Animations/Grunt/PushedState/Barehands/Loop/Grunt_barehands_pushed_loop.Grunt_barehands_pushed_loop | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bMirror）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Loop[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_bLoopable）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Loop[0].m_bLoopable[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fStartRatio）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Loop[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Loop）[0] → 未核中文义（m_fPlayRate）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Loop[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_StateMoveDynamic）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Movement[0].m_StateMoveDynamic[0] | /Game/DB/Hit/PushedFromGrabDynamic.PushedFromGrabDynamic | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fStateDistance）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Movement[0].m_fStateDistance[0] | 500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_PushedFromGrabbedReaction）[0] → 未核中文义（m_Movement）[0] → 未核中文义（m_fDuration）[0] | m_PushedReaction[0].m_PushedFromGrabbedReaction[0].m_Movement[0].m_fDuration[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_EnvAttackRanges）[0] | m_PushedReaction[0].m_EnvAttackRanges[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_EnvAttackRanges）[1] | m_PushedReaction[0].m_EnvAttackRanges[1] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_EnvAttackRanges）[2] | m_PushedReaction[0].m_EnvAttackRanges[2] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_EnvAttackRanges）[3] | m_PushedReaction[0].m_EnvAttackRanges[3] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_fAttackEnvCapsuleExtent）[0] | m_PushedReaction[0].m_fAttackEnvCapsuleExtent[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_fEnvAttackMaxAngleDeg）[0] | m_PushedReaction[0].m_fEnvAttackMaxAngleDeg[0] | 70 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_fEnvAttackMaxAngleWitoutSnapDeg）[0] | m_PushedReaction[0].m_fEnvAttackMaxAngleWitoutSnapDeg[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_fNavigationCostHeuristicScale）[0] | m_PushedReaction[0].m_fNavigationCostHeuristicScale[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_fNavigationMaxPathCost）[0] | m_PushedReaction[0].m_fNavigationMaxPathCost[0] | 2000 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PushedReaction）[0] → 未核中文义（m_EnvAttackImpactBoneName）[0] | m_PushedReaction[0].m_EnvAttackImpactBoneName[0] | custom_joint_06 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FallFromPushedAnim）[0] → 未核中文义（m_animation）[0] | m_FallFromPushedAnim[0].m_animation[0] | /Game/Animations/Grunt/PushedState/Barehands/Loop/Grunt_barehands_pushedFalling_loop.Grunt_barehands_pushedFalling_loop | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FallFromPushedAnim）[0] → 未核中文义（m_bMirror）[0] | m_FallFromPushedAnim[0].m_bMirror[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FallFromPushedAnim）[0] → 未核中文义（m_bLoopable）[0] | m_FallFromPushedAnim[0].m_bLoopable[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FallFromPushedAnim）[0] → 未核中文义（m_fStartRatio）[0] | m_FallFromPushedAnim[0].m_fStartRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FallFromPushedAnim）[0] → 未核中文义（m_fPlayRate）[0] | m_FallFromPushedAnim[0].m_fPlayRate[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Parent）[0] | m_Parent[0] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB.Yang_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（NativeClass）[0] | NativeClass[0] | /Script/Sifu.AttackPropertiesResistanceDB | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz；exports/state-reaction-settings.csv；exports/state-resistance-matrices.csv。引用到具体敌人的关系见 [[03配置/敌人原型/索引]]。
