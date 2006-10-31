Summary:	Indeo 4.1 codec for XAnim
Summary(pl):	Kodek Indeo 4.1 dla XAnima
Name:		xanim-codec-iv41
Version:	1.1
Release:	1
License:	non-distributable, for use with xanim exclusively
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv41_1.1_linuxELFx86c6.tgz
# NoSource1-md5:	c2db65ae5a3662310ac3d128d548d313
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv41_1.1_linuxELFalphaC6.tgz
# NoSource2-md5:	ab8bd9aae39b69ea98bd10be28b7fb20
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_iv41_1.1_linuxELFppc.tgz
# NoSource3-md5:	0ae42cfb65befa977c3acc55d69770a1
NoSource:	1
NoSource:	2
NoSource:	3
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Intel Indeo 4.1 codec decompression DLL for XAnim.

%description -l pl
Biblioteka do dekompresji kodeka Intel Indeo 4.1 dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_iv41_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc iv41.readme
%attr(755,root,root) %{_libdir}/xanim/vid_iv41_*.xa
