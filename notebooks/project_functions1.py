<<<<<<< HEAD
<<<<<<< HEAD
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48a5ff98-dcf9-4c68-ae4d-7e41a4519d8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_and_process('../data/raw/android-games.csv'):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv('../data/raw/android-games.csv')\n",
    "          .dropna(how=\"any\")\n",
    "          .sort_values(\"installs\")\n",
    "          .reset_index(drop=True)\n",
    "      )\n",
    "\n",
    "    # Method Chain 2 (Create new columns, drop others, and do processing)\n",
    "\n",
    "    df2 = (\n",
    "          df1\n",
    "      )\n",
    "\n",
    "    # Make sure to return the latest dataframe\n",
    "\n",
    "    return df2 "
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
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
=======
=======
import pandas as pd

>>>>>>> 6e0484f1820dc7e96e70a476dd54e5cf878f1263
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .dropna(how="any")
          .sort_values("installs")
          .reset_index(drop=True)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
      )

    # Make sure to return the latest dataframe

    return df2 
>>>>>>> 25b2f1cb597405d56e77c164a6ef832a71caae67
