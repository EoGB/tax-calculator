# HMT Tax Calculator

The main recursive tax calculation tool for HM Treasury.

More help is provided within the tool itself found [here](https://eogb.github.io/tax-calculator/), but a brief overview is below.

You can enter your tax bands, brackets, and citizen's salary, and it will follow a recursive banded tax formula to tax the width of each band that the salary encompasses at the percentage you have for said band.
It will also tax the portion of salary that does not fully cover a band at the percentage for the band it lies in, and can account for personal allowance in tax by setting the first band value greater than 0.
