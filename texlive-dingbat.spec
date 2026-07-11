%global tl_name dingbat
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Two dingbat symbol fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dingbat
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dingbat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts (ark10 and dingbat) are specified in Metafont; support macros
are provided for use in LaTeX. An Adobe Type 1 version of the fonts is
available in the niceframe fonts bundle.

