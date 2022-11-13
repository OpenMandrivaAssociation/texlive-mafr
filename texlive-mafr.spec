Name:		texlive-mafr
Version:	15878
Release:	1
Summary:	Mathematics in accord with French usage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mafr
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mafr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mafr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides settings and macros for typesetting
mathematics with LaTeX in compliance with French usage. It
comes with two document classes, 'fiche' and 'cours', useful to
create short high school documents such as tests or lessons.
The documentation is in French.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mafr/cours.cls
%{_texmfdistdir}/tex/latex/mafr/fiche.cls
%{_texmfdistdir}/tex/latex/mafr/mafr.sty
%doc %{_texmfdistdir}/doc/latex/mafr/ALIRE
%doc %{_texmfdistdir}/doc/latex/mafr/COPYING
%doc %{_texmfdistdir}/doc/latex/mafr/README
%doc %{_texmfdistdir}/doc/latex/mafr/docmafr.pdf
%doc %{_texmfdistdir}/doc/latex/mafr/docmafr.tex
%doc %{_texmfdistdir}/doc/latex/mafr/triangle.eps

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
