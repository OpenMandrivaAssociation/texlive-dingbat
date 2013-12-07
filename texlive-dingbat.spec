# revision 27918
# category Package
# catalog-ctan /fonts/dingbat
# catalog-date 2012-06-28 23:28:54 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-dingbat
Version:	1.0
Release:	5
Summary:	Two dingbat symbol fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dingbat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts (ark10 and dingbat) are specified in Metafont;
support macros are provided for use in LaTeX. An Adobe Type 1
version of the fonts is available in the niceframe fonts
bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/dingbat/ark10.mf
%{_texmfdistdir}/fonts/source/public/dingbat/dingbat.mf
%{_texmfdistdir}/fonts/tfm/public/dingbat/ark10.tfm
%{_texmfdistdir}/fonts/tfm/public/dingbat/dingbat.tfm
%{_texmfdistdir}/tex/latex/dingbat/dingbat.sty
%{_texmfdistdir}/tex/latex/dingbat/uark.fd
%{_texmfdistdir}/tex/latex/dingbat/udingbat.fd
%doc %{_texmfdistdir}/doc/fonts/dingbat/README
%doc %{_texmfdistdir}/doc/fonts/dingbat/dingbat.pdf
%doc %{_texmfdistdir}/doc/fonts/dingbat/dingbat.tex
#- source
%doc %{_texmfdistdir}/source/latex/dingbat/dingbat.dtx
%doc %{_texmfdistdir}/source/latex/dingbat/dingbat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
