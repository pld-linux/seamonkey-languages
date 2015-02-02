# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=2.32
U=http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$V/langpack/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for SeaMonkey
Summary(pl.UTF-8):	Pakiety językowe dla SeaMonkeya
Name:		seamonkey-languages
Version:	2.32
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.be.langpack.xpi
# Source0-md5:	a3ff3033579fa437ea1e993a27b47079
Source1:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ca.langpack.xpi
# Source1-md5:	0fbfd82fc613db70e78b452ec270e53e
Source2:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.cs.langpack.xpi
# Source2-md5:	c1c0a5721c7cf19e6c53e8a48e7cfa97
Source3:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.de.langpack.xpi
# Source3-md5:	d869d6b806fb16156e9608cb315247ed
Source4:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-GB.langpack.xpi
# Source4-md5:	a85dd6a7c0f61c55977503703b971c89
Source5:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-US.langpack.xpi
# Source5-md5:	e94165b33c63b898eeb06e443db67559
Source6:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-AR.langpack.xpi
# Source6-md5:	b89620c379e5c47cea1b08d3c3479651
Source7:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-ES.langpack.xpi
# Source7-md5:	e4e19148015cb708f993b8208a56cb3f
Source8:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fi.langpack.xpi
# Source8-md5:	d6462db0eb33d78d711981c04d34cee7
Source9:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fr.langpack.xpi
# Source9-md5:	7c576f623f3cd931c903b47b1952571d
Source10:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.gl.langpack.xpi
# Source10-md5:	8948dac7349186c8cd8a8c5fc2a62e11
Source11:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.hu.langpack.xpi
# Source11-md5:	5cf9968792e1479c7fb1b5ce3e816006
Source12:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.it.langpack.xpi
# Source12-md5:	e7bb16f4da74b82008534dffa4a185f8
Source13:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ja.langpack.xpi
# Source13-md5:	8a7525e9e3c0e612af512a7ff7852518
Source14:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.lt.langpack.xpi
# Source14-md5:	b1dded9bbc8046f049f6d2de3362b202
Source15:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nb-NO.langpack.xpi
# Source15-md5:	7227266817af998166d5ca3d7c5ecbbf
Source16:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nl.langpack.xpi
# Source16-md5:	cc5defe838a9e6dc02bca1c94cd83784
Source17:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pl.langpack.xpi
# Source17-md5:	6b12b0b9184ec62fc00964f901ad5327
Source18:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pt-PT.langpack.xpi
# Source18-md5:	75f8b340d7c22b65297ef8c5891df159
Source19:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ru.langpack.xpi
# Source19-md5:	a43a6bef3ce994c4867800c70138f785
Source20:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sk.langpack.xpi
# Source20-md5:	c9f79c73a1133639ddfdd76da1d9edf8
Source21:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sv-SE.langpack.xpi
# Source21-md5:	f5d25c144c359c904bd681c28c20bbf0
Source22:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.tr.langpack.xpi
# Source22-md5:	7a47c3dcc2d910ecbb772aad7355ab84
Source23:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.uk.langpack.xpi
# Source23-md5:	591e6d7eed2c066fceadcbb2454867dc
Source24:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-CN.langpack.xpi
# Source24-md5:	a2d7ee9f0e5bb79ab2ec60e2847c5572
Source25:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-TW.langpack.xpi
# Source25-md5:	6641cd8fecd464c9ce47c7f3f66a6418
URL:		http://www.seamonkey-project.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		seamonkeydir	%{_datadir}/seamonkey

%description
Language packs for SeaMonkey.

%description -l pl.UTF-8
Pakiety językowe dla SeaMonkeya.

%package -n seamonkey-lang-be
Summary:	Belarusian resources for SeaMonkey
Summary(pl.UTF-8):	Białoruskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-be
Belarusian resources for SeaMonkey.

%description -n seamonkey-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-ca
Summary:	Catalan resources for SeaMonkey
Summary(ca.UTF-8):	Recursos catalans per SeaMonkey
Summary(es.UTF-8):	Recursos catalanes para SeaMonkey
Summary(pl.UTF-8):	Katalońskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-ca
Catalan resources for SeaMonkey.

%description -n seamonkey-lang-ca -l ca.UTF-8
Recursos catalans per SeaMonkey.

%description -n seamonkey-lang-ca -l es.UTF-8
Recursos catalanes para SeaMonkey.

%description -n seamonkey-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-cs
Summary:	Czech resources for SeaMonkey
Summary(pl.UTF-8):	Czeskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-cs
Czech resources for SeaMonkey.

%description -n seamonkey-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-de
Summary:	German resources for SeaMonkey
Summary(pl.UTF-8):	Niemieckie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-de
German resources for SeaMonkey.

%description -n seamonkey-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-en_GB
Summary:	English (British) resources for SeaMonkey
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-en_GB
English (British) resources for SeaMonkey.

%description -n seamonkey-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-en_US
Summary:	English (American) resources for SeaMonkey
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-en_US
English (American) resources for SeaMonkey.

%description -n seamonkey-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-es_AR
Summary:	Spanish (Andorra) resources for SeaMonkey
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per SeaMonkey
Summary(es.UTF-8):	Recursos españoles (Andorra) para SeaMonkey
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Andory)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-es_AR
Spanish (Spain) resources for SeaMonkey.

%description -n seamonkey-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per SeaMonkey.

%description -n seamonkey-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para SeaMonkey.

%description -n seamonkey-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Andory).

%package -n seamonkey-lang-es
Summary:	Spanish (Spain) resources for SeaMonkey
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per SeaMonkey
Summary(es.UTF-8):	Recursos españoles (España) para SeaMonkey
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Hiszpanii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-es
Spanish (Spain) resources for SeaMonkey.

%description -n seamonkey-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per SeaMonkey.

%description -n seamonkey-lang-es -l es.UTF-8
Recursos españoles (España) para SeaMonkey.

%description -n seamonkey-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla SeaMonkeya (wersja dla Hiszpanii).

%package -n seamonkey-lang-fi
Summary:	Finnish resources for SeaMonkey
Summary(pl.UTF-8):	Fińskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-fi
Finnish resources for SeaMonkey.

%description -n seamonkey-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-fr
Summary:	French resources for SeaMonkey
Summary(pl.UTF-8):	Francuskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-fr
French resources for SeaMonkey.

%description -n seamonkey-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-gl
Summary:	Galician resources for SeaMonkey
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-gl
Galician resources for SeaMonkey.

%description -n seamonkey-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-hu
Summary:	Hungarian resources for SeaMonkey
Summary(hu.UTF-8):	Magyar nyelv SeaMonkey-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-hu
Hungarian resources for SeaMonkey.

%description -n seamonkey-lang-hu -l hu.UTF-8
Magyar nyelv SeaMonkey-hez.

%description -n seamonkey-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-it
Summary:	Italian resources for SeaMonkey
Summary(pl.UTF-8):	Włoskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-it
Italian resources for SeaMonkey.

%description -n seamonkey-lang-it -l pl.UTF-8
Włoskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-ja
Summary:	Japanese resources for SeaMonkey
Summary(pl.UTF-8):	Japońskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-ja
Japanese resources for SeaMonkey.

%description -n seamonkey-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-lt
Summary:	Lithuanian resources for SeaMonkey
Summary(pl.UTF-8):	Litewskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-lt
Lithuanian resources for SeaMonkey.

%description -n seamonkey-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-nb
Summary:	Norwegian Bokmaal resources for SeaMonkey
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-nb
Norwegian Bokmaal resources for SeaMonkey.

%description -n seamonkey-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-nl
Summary:	Dutch resources for SeaMonkey
Summary(pl.UTF-8):	Holenderskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-nl
Dutch resources for SeaMonkey.

%description -n seamonkey-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-pl
Summary:	Polish resources for SeaMonkey
Summary(pl.UTF-8):	Polskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-pl
Polish resources for SeaMonkey.

%description -n seamonkey-lang-pl -l pl.UTF-8
Polskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-pt
Summary:	Portuguese (Portugal) resources for SeaMonkey
Summary(pl.UTF-8):	Portugalskie pliki językowe dla SeaMonkeya (wersja dla Portugalii)
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-pt
Portuguese (Portugal) resources for SeaMonkey.

%description -n seamonkey-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla SeaMonkeya (wersja dla Portugalii).

%package -n seamonkey-lang-ru
Summary:	Russian resources for SeaMonkey
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-ru
Russian resources for SeaMonkey.

%description -n seamonkey-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-sk
Summary:	Slovak resources for SeaMonkey
Summary(pl.UTF-8):	Słowackie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-sk
Slovak resources for SeaMonkey.

%description -n seamonkey-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-sv
Summary:	Swedish resources for SeaMonkey
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-sv
Swedish resources for SeaMonkey.

%description -n seamonkey-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-tr
Summary:	Turkish resources for SeaMonkey
Summary(pl.UTF-8):	Tureckie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-tr
Turkish resources for SeaMonkey.

%description -n seamonkey-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-uk
Summary:	Ukrainian resources for SeaMonkey
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-uk
Ukrainian resources for SeaMonkey.

%description -n seamonkey-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-zh_CN
Summary:	Simplified Chinese resources for SeaMonkey
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-zh_CN
Simplified Chinese resources for SeaMonkey.

%description -n seamonkey-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla SeaMonkeya.

%package -n seamonkey-lang-zh_TW
Summary:	Traditional Chinese resources for SeaMonkey
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla SeaMonkeya
Group:		I18n
Requires:	seamonkey >= %{version}
Provides:	seamonkey-lang-resources = %{version}

%description -n seamonkey-lang-zh_TW
Traditional Chinese resources for SeaMonkey.

%description -n seamonkey-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla SeaMonkeya.

%prep
unpack() {
    local args="$1" file="$2"
	base=$(basename $file)
	local lang=$(basename $file .langpack.xpi)
	lang=${lang##seamonkey-%{version}.}
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 25 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{seamonkeydir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .langpack.xpi)
	basename=${basename##seamonkey-%{version}.}
	cp -p $a $RPM_BUILD_ROOT%{seamonkeydir}/extensions/langpack-$basename@seamonkey.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n seamonkey-lang-be
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-be@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-ca
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-ca@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-cs
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-cs@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-de
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-de@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-en_GB
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-en-GB@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-en_US
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-en-US@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-es_AR
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-es-AR@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-es
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-es-ES@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-fi
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-fi@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-fr
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-fr@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-gl
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-gl@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-hu
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-hu@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-it
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-it@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-ja
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-ja@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-lt
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-lt@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-nb
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-nb-NO@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-nl
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-nl@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-pl
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-pl@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-pt
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-pt-PT@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-ru
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-ru@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-sk
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-sk@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-sv
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-sv-SE@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-tr
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-tr@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-uk
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-uk@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-zh_CN
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-zh-CN@seamonkey.mozilla.org.xpi

%files -n seamonkey-lang-zh_TW
%defattr(644,root,root,755)
%{seamonkeydir}/extensions/langpack-zh-TW@seamonkey.mozilla.org.xpi
