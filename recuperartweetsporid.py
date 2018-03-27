# -*- coding: utf-8 -*-

#    This file is part of escucharTweets.
#
#    escucharTweets is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    escucharTweets is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with escucharTweets; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging
import tweepy
import ConfigManager
import csv
import time

logger = logging.getLogger(__name__)


def iniciar():
        config = ConfigManager.ConfigManager()
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        with open('Salida.csv', 'wt', encoding='utf8') as csvfilew:
                spamwriter = csv.writer(csvfilew, delimiter=';',
                                        quotechar='"', quoting=csv.QUOTE_ALL)
                with open('tweetsabuscar.csv', 'rt') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter='\t')
                        for row in spamreader:
                                try:
                                        a = api.get_status(row[0])
                                        lineas = []
                                        lineas.append(a.text)
                                        lineas.append(a.retweet_count)
                                        lineas.append(a.favorite_count)
                                        lineas.append(a.truncated)
                                        lineas.append(a.id_str)
                                        lineas.append(a.in_reply_to_screen_name)
                                        lineas.append(a.source_url)
                                        lineas.append(a.retweeted)
                                        lineas.append(a.created_at)
                                        lineas.append(a.in_reply_to_status_id_str)
                                        lineas.append(a.in_reply_to_user_id_str)
                                        lineas.append(a.lang)
                                        lineas.append(a.user.listed_count)
                                        lineas.append(a.user.verified)

                                        lineas.append(a.user.location)
                                        lineas.append(a.user.verified)
                                        lineas.append(a.user.verified)
                                        lineas.append(a.user.id)
                                        lineas.append(a.user.description)
                                        lineas.append(a.user.geo_enabled)
                                        lineas.append(a.user.created_at)
                                        lineas.append(a.user.statuses_count)
                                        lineas.append(a.user.followers_count)
                                        lineas.append(a.user.protected)
                                        lineas.append(a.user.url)
                                        lineas.append(a.user.name)
                                        lineas.append(a.user.time_zone)
                                        lineas.append(a.user.lang)
                                        lineas.append(a.user.utc_offset)
                                        lineas.append(a.user.friends_count)
                                        lineas.append(a.user.screen_name)

                                        if (a.place):
                                                lineas.append(a.place.country_code)
                                                lineas.append(a.place.country)
                                                lineas.append(a.place.place_type)
                                                lineas.append(a.place.full_name)
                                                lineas.append(a.place.name)
                                                lineas.append(a.place.id)
                                                lineas.append(a.place.full_name)
                                                lineas.append(a.place.url)
                                        else:
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                                lineas.append(b'')
                                        lineas.append(b'')
                                        lineas.append(b'')
                                        lineas.append(b'')
                                        lineas.append(b'')
                                        lineas.append(b'')
                                        lineas.append(b'')

                                        spamwriter.writerow(lineas)
                                except tweepy.RateLimitError:
                                        print("limite alcanzado esperando")
                                        time.sleep(5)
                                except Exception as ex:
                                        if(hasattr(ex, 'code') is False):
                                                print(ex)


iniciar()