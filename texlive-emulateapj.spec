%global tl_name emulateapj
%global tl_revision 74166

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Produce output similar to that of APJ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/emulateapj
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX class (based on current RevTeX) to produce preprints with the
page layout similar to that of the Astrophysical Journal.

