{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas\n",
    "\n",
    "df1 = pandas.read_csv(\"supermarkets.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>ID</th>\n",
       "      <th>Address</th>\n",
       "      <th>City</th>\n",
       "      <th>State</th>\n",
       "      <th>Country</th>\n",
       "      <th>Name</th>\n",
       "      <th>Employees</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>3666 21st St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>CA 94114</td>\n",
       "      <td>USA</td>\n",
       "      <td>Madeira</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>735 Dolores St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>CA 94119</td>\n",
       "      <td>USA</td>\n",
       "      <td>Bready Shop</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>332 Hill St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>California 94114</td>\n",
       "      <td>USA</td>\n",
       "      <td>Super River</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>3995 23rd St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>CA 94114</td>\n",
       "      <td>USA</td>\n",
       "      <td>Ben's Shop</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1056 Sanchez St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>California</td>\n",
       "      <td>USA</td>\n",
       "      <td>Sanchez</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>551 Alvarado St</td>\n",
       "      <td>San Francisco</td>\n",
       "      <td>CA 94114</td>\n",
       "      <td>USA</td>\n",
       "      <td>Richvalley</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID          Address           City             State Country         Name  \\\n",
       "0   1     3666 21st St  San Francisco          CA 94114     USA      Madeira   \n",
       "1   2   735 Dolores St  San Francisco          CA 94119     USA  Bready Shop   \n",
       "2   3      332 Hill St  San Francisco  California 94114     USA  Super River   \n",
       "3   4     3995 23rd St  San Francisco          CA 94114     USA   Ben's Shop   \n",
       "4   5  1056 Sanchez St  San Francisco        California     USA      Sanchez   \n",
       "5   6  551 Alvarado St  San Francisco          CA 94114     USA   Richvalley   \n",
       "\n",
       "   Employees  \n",
       "0          8  \n",
       "1         15  \n",
       "2         25  \n",
       "3         10  \n",
       "4         12  \n",
       "5         20  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'geopy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-99b9d2081153>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mgeopy\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'geopy'"
     ]
    }
   ],
   "source": [
    "import geopy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'geopy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-5-99b9d2081153>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mgeopy\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'geopy'"
     ]
    }
   ],
   "source": [
    "import geopy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'geopy'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-0cba84341fb3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mgeopy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgeocoders\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mNominatim\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mnom\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mNominatim\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'geopy'"
     ]
    }
   ],
   "source": [
    "from geopy.geocoders import Nominatim\n",
    "nom = Nominatim()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
