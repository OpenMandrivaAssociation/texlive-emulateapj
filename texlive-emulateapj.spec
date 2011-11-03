# revision 16099
# category Package
# catalog-ctan /macros/latex/contrib/emulateapj
# catalog-date 2009-12-25 00:35:43 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-emulateapj
Version:	20091225
Release:	1
Summary:	Produce output similar to that of APJ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/emulateapj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/emulateapj.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX class (based on current RevTeX) to produce preprints
with the page layout similar to that of the Astrophysical
Journal.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/emulateapj/emulateapj.cls
%doc %{_texmfdistdir}/doc/latex/emulateapj/README
%doc %{_texmfdistdir}/doc/latex/emulateapj/sample.pdf
%doc %{_texmfdistdir}/doc/latex/emulateapj/sample.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
