#Usage:
#./convert2UTF8.sh /path/to/folder subfix
#e.g: deal with *.chs.srt subs
#./convert2UTF8.sh /path/to/folder tex

cd $1

#using enca to convert chinese encodings (such as GBK, BIG5, HZ) to utf8
#english sub convertion is not included
#enca can convert dos format to unix by itself
for f in *.$2
do
    enca -L zh -x UTF-8 < $f > $f.utf8
    mv $f.utf8 $f
done

#using iconv
#dos2unix *$2.srt
#for f in *big5.srt;do iconv -f big5 -t utf-8 "$f" -o "$f".utf8.srt;mv "$f".utf8.srt "$f"; done
#for f in *gb.srt;do iconv -f gb18030 -t utf-8 "$f" -o "$f".utf8.srt;mv "$f".utf8.srt "$f"; done
#for f in *$2.srt;do iconv -f $3 -t utf-8 "$f" -o "$f".utf8.srt;mv "$f".utf8.srt "$f"; done
