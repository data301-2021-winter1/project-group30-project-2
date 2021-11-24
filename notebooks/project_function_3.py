{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6b9fcedf-2c32-4e4c-809b-3732140cb8c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PROJECT FUNCTION 3\n"
     ]
    }
   ],
   "source": [
    "print('PROJECT FUNCTION 3')\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "def load_and_process(url_or_path_to_csv_file):\n",
    "\n",
    "    # Method Chain 1 (Load data and deal with missing data)\n",
    "\n",
    "    df1 = (\n",
    "          pd.read_csv(url_or_path_to_csv_file)\n",
    "          .dropna(how=\"any\")\n",
    "          .sort_values(\"category\")\n",
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c02721e6-fe75-4c8d-9607-ad54873d219a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
