{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "##libraries needed\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Fixing columns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Wage</th>\n",
       "      <th>Age</th>\n",
       "      <th>Club</th>\n",
       "      <th>League</th>\n",
       "      <th>Nation</th>\n",
       "      <th>Position</th>\n",
       "      <th>Apps</th>\n",
       "      <th>Caps</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>46427.0</td>\n",
       "      <td>23</td>\n",
       "      <td>PSG</td>\n",
       "      <td>Ligue 1 Uber Eats</td>\n",
       "      <td>FRA</td>\n",
       "      <td>Forward</td>\n",
       "      <td>190</td>\n",
       "      <td>57</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>42125.0</td>\n",
       "      <td>30</td>\n",
       "      <td>PSG</td>\n",
       "      <td>Ligue 1 Uber Eats</td>\n",
       "      <td>BRA</td>\n",
       "      <td>Midfilder</td>\n",
       "      <td>324</td>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>34821.0</td>\n",
       "      <td>35</td>\n",
       "      <td>PSG</td>\n",
       "      <td>Ligue 1 Uber Eats</td>\n",
       "      <td>ARG</td>\n",
       "      <td>Forward</td>\n",
       "      <td>585</td>\n",
       "      <td>162</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19959.0</td>\n",
       "      <td>31</td>\n",
       "      <td>R. Madrid</td>\n",
       "      <td>La Liga</td>\n",
       "      <td>BEL</td>\n",
       "      <td>Forward</td>\n",
       "      <td>443</td>\n",
       "      <td>120</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19500.0</td>\n",
       "      <td>31</td>\n",
       "      <td>Man UFC</td>\n",
       "      <td>Premier League</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Goalkeeper</td>\n",
       "      <td>480</td>\n",
       "      <td>45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3902</th>\n",
       "      <td>3.4</td>\n",
       "      <td>19</td>\n",
       "      <td>Vigo</td>\n",
       "      <td>La Liga</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Defender</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3903</th>\n",
       "      <td>3.2</td>\n",
       "      <td>18</td>\n",
       "      <td>Famalicao</td>\n",
       "      <td>Primiera Liga</td>\n",
       "      <td>BRA</td>\n",
       "      <td>Goalkeeper</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3904</th>\n",
       "      <td>2.9</td>\n",
       "      <td>18</td>\n",
       "      <td>Vigo</td>\n",
       "      <td>La Liga</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Forward</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3905</th>\n",
       "      <td>2.7</td>\n",
       "      <td>18</td>\n",
       "      <td>Vigo</td>\n",
       "      <td>La Liga</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Defender</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3906</th>\n",
       "      <td>1.4</td>\n",
       "      <td>18</td>\n",
       "      <td>Vigo</td>\n",
       "      <td>La Liga</td>\n",
       "      <td>ESP</td>\n",
       "      <td>Defender</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3907 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         Wage  Age       Club             League Nation    Position  Apps  \\\n",
       "0     46427.0   23        PSG  Ligue 1 Uber Eats    FRA     Forward   190   \n",
       "1     42125.0   30        PSG  Ligue 1 Uber Eats    BRA   Midfilder   324   \n",
       "2     34821.0   35        PSG  Ligue 1 Uber Eats    ARG     Forward   585   \n",
       "3     19959.0   31  R. Madrid            La Liga    BEL     Forward   443   \n",
       "4     19500.0   31    Man UFC     Premier League    ESP  Goalkeeper   480   \n",
       "...       ...  ...        ...                ...    ...         ...   ...   \n",
       "3902      3.4   19       Vigo            La Liga    ESP    Defender     0   \n",
       "3903      3.2   18  Famalicao      Primiera Liga    BRA  Goalkeeper     0   \n",
       "3904      2.9   18       Vigo            La Liga    ESP     Forward     0   \n",
       "3905      2.7   18       Vigo            La Liga    ESP    Defender     0   \n",
       "3906      1.4   18       Vigo            La Liga    ESP    Defender     0   \n",
       "\n",
       "      Caps  \n",
       "0       57  \n",
       "1      119  \n",
       "2      162  \n",
       "3      120  \n",
       "4       45  \n",
       "...    ...  \n",
       "3902     0  \n",
       "3903     0  \n",
       "3904     0  \n",
       "3905     0  \n",
       "3906     0  \n",
       "\n",
       "[3907 rows x 8 columns]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soccer_df = pd.read_csv('SalaryPrediction.csv')\n",
    "soccer_df['Wage'] = soccer_df['Wage'].str.replace(',','').astype(int)\n",
    "soccer_df['Wage'] = soccer_df['Wage']/1000\n",
    "soccer_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Boxplot of each league"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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MHcCy8H4+Pi8bQCApeKEE06Ytw2jYGJi4v55WPft22f00xIxxMinxyX5k6r6YpKtSf53a+3jSX4zycaquinJxq6d1toNST6c5MtJPp7kVa21vd1jvTLJuzM9CfnXk0wu5gsBuOOOO+a077zzzoEqAQCY36233jpvG0bBli1bsnv37iTJ7t27s3nz5oErIklWLfYTttb+MsmPHKD/9iRnPsg2b0rypgP0b0vy9CNdI0dGVc1Z+ctEzIyiAy1ZfMUVVwxUDQDAg7NQCsvBxo0b87GPfSy7d+/O6tWrc/bZZw9dEhluwnGWgR/+4R+e0z711FMHqgT6Y8liAOBosf/q0z/4gz84TCHQo/Hx8fuD1RUrVpgWY4kQPtGbr3/963PaO3bsGKgS6I8jiADA0WL//fEbb7xxoEqgP2NjY9m0aVOqKps2bTK32RKx6KfdsXzcc88987ZhFMw+tfRAbQAAYHGNj49n586dRj0tIcInerNixYrs27dvThsAAAD6NDY2lssvv3zoMphFGkBvZgdPB2oDACwVY2Nj87ZhFOx/MNjBYWCx+LQBAGDZ++53vztvG0bBM57xjDntZz7zmQNVAiw3wicAAJa973//+/O2YRR89atfndP+yle+MlAlwHJjzid6s3Llyuzdu3dOGwAgSS677LIlvxLua17zmqFLSJKsX79+ydTC0c2CQMBQjHyiN2edddac9saNGweqBPqzatWqedsAAEvFmjVr5m0D9MWvJHrz0pe+NJ/4xCfub//sz/7sgNVAP170ohfl93//9+9v/7N/9s8GrAbg6LHURvJ88pOfzCWXXHJ/+w1veENe8IIXDFgRo2CpjfB77GMfm7vvvntOe6n8WzTCD0abkU/05nd+53fmtN///vcPVAn058orr5zTnh1EAXD0mD1ie+XKlYInRtKxxx57//UVK1bMaQP0ycgnenP11VfPaV911VV5wxveMEwx0JM9e/bM22bpW2pHpZeqm266KcnSG62yFDl6f/R60pOelL/+67/ORRddNHQpjIil+Fnw8z//8/nLv/zLvPnNb87pp58+dDnQi6mpqbzhDW/IxRdfnBNOOGHocojwCWBBTKx/9NuxY0e+cMMXkscMXckSt2/6zxdu/sKwdSx1dw1dAAtx/PHH5/jjjzfqiZF27LHH5rTTThM8MdImJiayffv2TExM5Jd/+ZeH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",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20, 10))\n",
    "sns.boxplot(x='League',y='Wage',data=soccer_df)\n",
    "plt.yticks(range(0,50000,5000))\n",
    "plt.plot()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## average salary by age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pandas.core.groupby.generic.DataFrameGroupBy object at 0x169071e50>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "age_df = soccer_df.groupby('Age')\n",
    "age_df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
