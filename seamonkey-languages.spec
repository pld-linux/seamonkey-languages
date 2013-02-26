# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=2.10
U=http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/$V/langpack/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for SeaMonkey
Summary(pl.UTF-8):	Pakiety językowe dla SeaMonkeya
Name:		seamonkey-languages
Version:	2.15.2
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.be.langpack.xpi
# Source0-md5:	00b81ee6f1e7e205902faa7d6d27eefe
Source1:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ca.langpack.xpi
# Source1-md5:	80e994edc2c3073ab58c77085474c165
Source2:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.cs.langpack.xpi
# Source2-md5:	13dde1167dbe0437ebc78622f7c66dee
Source3:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.de.langpack.xpi
# Source3-md5:	b0f8d81d7f395538848cbd23881e5575
Source4:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-GB.langpack.xpi
# Source4-md5:	9765a2ed0c2326088aa898a8436aebae
Source5:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.en-US.langpack.xpi
# Source5-md5:	eb7b97fa5b22587045547bdead9af201
Source6:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-AR.langpack.xpi
# Source6-md5:	c3a054a0dc5aacf703844f11812122aa
Source7:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.es-ES.langpack.xpi
# Source7-md5:	ae4257d135e92e50ece65053076fdf75
Source8:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fi.langpack.xpi
# Source8-md5:	ea805c12532808266393823c0fe88348
Source9:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.fr.langpack.xpi
# Source9-md5:	f926773dd2e20030903baf774a80f63a
Source10:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.gl.langpack.xpi
# Source10-md5:	ba79f779df0535ac02de9c10a72b23e3
Source11:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.hu.langpack.xpi
# Source11-md5:	215731157a2227f7cb225b6d631eafa0
Source12:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.it.langpack.xpi
# Source12-md5:	446510f802d55b1f871f718ed902a605
Source13:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ja.langpack.xpi
# Source13-md5:	101ddd876028f6cd9360408a86af9480
Source14:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.lt.langpack.xpi
# Source14-md5:	07b5295dc2559dc9da1b47da8da1499d
Source15:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nb-NO.langpack.xpi
# Source15-md5:	4a8e439bf3794678987a79de62136243
Source16:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.nl.langpack.xpi
# Source16-md5:	e9fc61e614682baac3d7a95cb7fa6086
Source17:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pl.langpack.xpi
# Source17-md5:	b44bdbd0edf784d8ad7a07fe030e6dd3
Source18:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.pt-PT.langpack.xpi
# Source18-md5:	62a8f8848e7d633a08997d0e7d32593a
Source19:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.ru.langpack.xpi
# Source19-md5:	f5b697fa22a5ee278ed0465d65377fcf
Source20:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sk.langpack.xpi
# Source20-md5:	560073e7076f7c17e33f886bfdca268b
Source21:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.sv-SE.langpack.xpi
# Source21-md5:	308d50d166e832b8a9a758b9cff5ae00
Source22:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.tr.langpack.xpi
# Source22-md5:	31a85fc9bfb8fb9d5d9fe49f56b1006c
Source23:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.uk.langpack.xpi
# Source23-md5:	ae29f97fa7e0429de71d45e657593b68
Source24:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-CN.langpack.xpi
# Source24-md5:	6a2d4f8630f78b833e98939361dd36bf
Source25:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/langpack/seamonkey-%{version}.zh-TW.langpack.xpi
# Source25-md5:	69ed7e27d7e20f366024f8f7c2af5f7f
URL:		http://www.seamonkey-project.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
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
