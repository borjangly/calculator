Reference: https://strategywiki.org/wiki/MapleStory/Formulas

WORK IN PROGRESS

## Total Stat

$$TotalStat = (AP \times (1 + AP\%) + BaseStat)\times(1+Stat\%) + FinalStat$$

Solving for base stat:

$$TotalStat = (AP \times (1 + AP\%) + BaseStat)\times(1+Stat\%) + FinalStat$$

$$TotalStat - FinalStat = (AP \times (1 + AP\%) + BaseStat)\times(1+Stat\%)$$

$$\dfrac{TotalStat - FinalStat}{(1+Stat\%)} = AP \times (1 + AP\%) + BaseStat$$

$$ BaseStat = \dfrac{TotalStat - FinalStat}{(1+Stat\%)} - AP \times (1 + AP\%)$$


Define the function mapping an increase in base stats $n$ to the increase in total stats as $i(n)$. For any increase in base stat, the resulting total stat increase can be measured as:

$$i(n) = NewTotalStat - TotalStat$$

$$i(n) = (AP \times (1 + AP\%) + (BaseStat + n))\times(1+Stat\%) + FinalStat - TotalStat$$

Substituting the expression for $BaseStat$ derived above

$$i(n) = \left(AP \times (1 + AP\%) + \dfrac{TotalStat - FinalStat}{(1+Stat\%)} - AP \times (1 + AP\%) + n \right) \times (1+Stat\%) + FinalStat - TotalStat$$

$$i(n) = \left(AP \times (1 + AP\%) - AP \times (1 + AP\%) + \dfrac{TotalStat - FinalStat}{(1+Stat\%)}  + n \right) \times (1+Stat\%) + FinalStat - TotalStat$$

$$i(n) = \left(\dfrac{TotalStat - FinalStat}{(1+Stat\%)}  + n \right) \times (1+Stat\%) + FinalStat - TotalStat$$

$$i(n) = TotalStat - FinalStat + n*(1+Stat\%) + FinalStat - TotalStat$$

$$i(n) = TotalStat - FinalStat + FinalStat - TotalStat + n*(1+Stat\%) $$

$$i(n) = n*(1+Stat\%) $$


## Attack Stuff

Assuming no sources of final attack, total attack is defined as 

$$TotalAttack = BaseAttack \times (1 + Attack\%)$$

An increase of a base attack will be $(BaseAttack + a) \times (1 + Attack\%)$

The percentage increase can be defined as 

$$p\_in =  \dfrac{(BaseAttack + a) \times (1 + Attack\%)}{BaseAttack \times (1 + Attack\%)}$$

$$p\_in =  1 + \dfrac{a}{BaseAttack}$$


## Attack:Primary Stat ratio

Match primary stat value % increase to $p\_in$

$$p\_in = \dfrac{(PrimaryStat * i(n) + FinalStat)\times4 + TotalSecondaryStat}{(PrimaryStat + FinalStat) *4 + TotalSecondaryStat}$$

$$p\_in = 1 + \dfrac{4i(n) \times PrimaryStat + 4FinalPrinaryStat + TotalSecondaryStat}{4TotalPrimaryStat + 4TotalFinalStat + TotalSecondaryStat}$$

$$p\_in = 1 + \left(i(n) PrimaryStat + 4FinalPrinaryStat + TotalSecondaryStat \right)

%{4TotalPrimaryStat + 4TotalFinalStat + TotalSecondaryStat}$$


$$p\_in = 1 + \dfrac{i(n)}{TotalPrimaryStat + \dfrac{TotalSecondaryStat}{4}}$$

Equating the two expressions

$$1 + \dfrac{a}{BaseAttack} = 1 + \dfrac{i(n)}{TotalPrimaryStat + \dfrac{TotalSecondaryStat}{4}}$$

$$\dfrac{a}{BaseAttack} = \dfrac{i(n)}{TotalPrimaryStat + \dfrac{TotalSecondaryStat}{4}}$$

$$\dfrac{a}{BaseAttack} = \dfrac{n*(1+Stat\%)}{TotalPrimaryStat + \dfrac{TotalSecondaryStat}{4}}$$

$$\dfrac{n}{a} = \dfrac{TotalPrimaryStat + \dfrac{TotalSecondaryStat}{4}}{BaseAttack \times (1 + Stat\%)}$$

E.g. For a Buccaneer with 72,825 STR, 10,195 DEX, 682 str% and 3,271 base attack, given an increase of $a = 1$ would have an attack:stat ratio of

$$\dfrac{n}{1} = \dfrac{72,825 + \dfrac{10,195}{4}}{3,271 \times (1 + 682\%)}$$

$$n = \dfrac{72,825 + 2,548.75}{3,271 \times 7.82}$$

$$n = 2.947$$

Thus the attack to stat ratio is $1:2.947$


## General Damage Formula

$$Output = SkillDamage\% \times WeaponMultiplier \times StatValue \times \dfrac{TotalAttack}{100} \times (1 + BossDamage\% + Damage\%) \\
\times (1 + 0.35 + CritDamage\%) \times (1 - \dfrac{MonsterDEF\%}{100} \times (1 - \dfrac{IgnoreEnemyDefense\%}{100}))$$

$SkillDamage\%$ and $WeaponMultiplier$ are constants. Simplifying all constants into $C$ gives us

$$Output = C \times StatValue \times TotalAttack \times (1 + BossDamage\% + Damage\%) \times (1 + 0.35 + CritDamage\%) \\ \times (1 - \dfrac{MonsterDEF\%}{100} \times (1 - \dfrac{IgnoreEnemyDefense\%}{100}))$$

### Stat Value

Stat value is defined as

$$StatValue = TotalPrimaryStat*4 + TotalSecondaryStat$$

### Total Attack

Total attack is defined as

$$TotalAttack = BaseAttack \times (1 + Attack\%) + FinalAttack$$