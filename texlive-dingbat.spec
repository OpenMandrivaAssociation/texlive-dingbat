Name:		texlive-dingbat
Version:	27918
Release:	2
Summary:	Two dingbat symbol fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dingbat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
