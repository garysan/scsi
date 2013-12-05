#!/bin/bash

TARGET=/var/lib/squidguard/db/blacklists

cd $TARGET || exit

# only run if squidGuard is active!
[ "`ps auxw | grep squid[G]uard`" ] || exit

rsync -az squidguard.mesd.k12.or.us::filtering $TARGET

for DIR in `ls $TARGET`
do
        if [ -f $DIR/domains.include ]
        then
                TMP=$RANDOM
                cat $DIR/domains $DIR/domains.include | sort | uniq > $DIR/domains.$TMP
                mv -f $DIR/domains.$TMP $DIR/domains
        fi
        if [ -f $DIR/urls.include ]
        then
                TMP=$RANDOM
                cat $DIR/urls $DIR/urls.include | sort | uniq > $DIR/urls.$TMP
                mv -f $DIR/urls.$TMP $DIR/urls
        fi
done

/usr/bin/squidGuard -c /etc/squid/squidGuard.conf  -C all
# /usr/sbin/squidGuard -c /etc/squid/squidGuard.conf  -u

chown -R proxy:proxy $TARGET
chown -R proxy:proxy /var/log/squid/squidGuard.log

sleep 5s

/usr/bin/killall -HUP squid
