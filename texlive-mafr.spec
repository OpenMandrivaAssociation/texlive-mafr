%global tl_name mafr
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Mathematics in accord with French usage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mafr
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mafr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mafr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides settings and macros for typesetting mathematics
with LaTeX in compliance with French usage. It comes with two document
classes, 'fiche' and 'cours', useful to create short high school
documents such as tests or lessons. The documentation is in French.

