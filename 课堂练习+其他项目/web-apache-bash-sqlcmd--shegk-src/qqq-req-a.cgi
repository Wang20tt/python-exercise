#!/bin/bash

echo "Content-type: text/html; charset=utf-8"
echo ""
if [ "$REQUEST_METHOD" = "GET" ] ; then
	echo "POST is expected"
	exit
fi

echo "<html>"
echo "<head>"
echo "<title>query req post ok</title>"
echo "</head>"
echo "<body>"

OIFS="$IFS"
IFS=\& 
read qqns qqqs qqnk go
IFS="$OIFS"
qqns=${qqns#qqns=}  # remove prefix 'qqns='
qqqs=${qqqs#qqqs=}  # 'qqqs='
qqnk=${qqnk#qqnk=}  # 'qqnk='
echo "qqnums: $qqns" 
#echo "groups: $qqqs"
#echo "qqnike: $qqnk" 

# last 100/20/10 only
qqns1=$(echo $qqns | sed -e 's/[^0-9]/ /g' | tr " " "\n" | sort | uniq | grep -v "^$" |
	awk '{ if ($1>10000 && $1<999999999999 && $1!=11348929) print($1)}'| tail -100 | tr "\n" " ")
echo "<br>num refined: $qqns1"  # dedup
sql1="select top 1000 * from [Member]"
where1=0
nn=0
for n in $qqns1 ; do 
	if [ $where1 -eq 0 ]; then 
		sql1="$sql1 where "
		where1=1
	else
		sql1="$sql1 or"
	fi
	sql1="$sql1 qqnum = $n "
	((nn=nn+1))
done

echo "<br>$sql1<br>"
echo "<pre>"
#ssh -l root 172.28.11.8 '"$sql1"'
/opt/mssql-tools/bin/sqlcmd -S 172.28.11.8 -U SA -P QQ12-shegk -d QQGroup -Q """""$sql1;"""""
echo "</pre>"
echo "<br> sql end"
echo "</body>"
echo "</html>"

exit
