# revision 28469
# category Package
# catalog-ctan /macros/latex/contrib/emulateapj
# catalog-date 2012-12-05 13:33:41 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-emulateapj
Version:	20180303
Release:	1
Summary:	Produce output similar to that of APJ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emulateapj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
