Name:           ksuperkey
Version:        0.4
Release:        2%{?dist}
Summary:        Enables the Super Key in KDE

License:        GPLv3
URL:            https://github.com/hanschen/ksuperkey
Source0:        https://github.com/hanschen/ksuperkey/archive/v%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  libX11-devel libXtst-devel

%description
ksuperkey allows you to open the application launcher in KDE Plasma Desktop using the Super key (also known as the "Windows key"). If you hold down the Super key it will still act as a modifier key, allowing you to use it for other keyboard shortcuts.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p %{buildroot}%{_datadir}/applications
install -m755 $RPM_BUILD_DIR/%{name}-%{version}/ksuperkey.desktop %{buildroot}%{_datadir}/applications

%files
%doc LICENSE README.md
%{_bindir}/ksuperkey
%{_datadir}/applications/ksuperkey.desktop

%changelog
* Wed Sep 2 2015 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 0.4-1
- First package
