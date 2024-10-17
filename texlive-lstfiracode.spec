Name:		texlive-lstfiracode
Version:	49503
Release:	2
Summary:	Use Fira Code font for listings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lstfiracode
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstfiracode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lstfiracode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The lstfiracode package defines FiraCodeStyle for the use with
the listings package. This style contains almost all ligatures
in Nikita Prokopov's Fira Code family of fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lstfiracode
%doc %{_texmfdistdir}/doc/latex/lstfiracode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
