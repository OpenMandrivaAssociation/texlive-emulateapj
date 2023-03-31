Name:		texlive-emulateapj
Version:	28469
Release:	2
Summary:	Produce output similar to that of APJ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emulateapj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX class (based on current RevTeX) to produce preprints
with the page layout similar to that of the Astrophysical
Journal.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emulateapj/emulateapj.cls
%doc %{_texmfdistdir}/doc/latex/emulateapj/README
%doc %{_texmfdistdir}/doc/latex/emulateapj/sample.pdf
%doc %{_texmfdistdir}/doc/latex/emulateapj/sample.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
