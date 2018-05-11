#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : curl
Version  : 7.59.0
Release  : 75
URL      : https://github.com/curl/curl/releases/download/curl-7_59_0/curl-7.59.0.tar.bz2
Source0  : https://github.com/curl/curl/releases/download/curl-7_59_0/curl-7.59.0.tar.bz2
Source99 : https://github.com/curl/curl/releases/download/curl-7_59_0/curl-7.59.0.tar.bz2.asc
Summary  : Library to transfer files with ftp, http, etc.
Group    : Development/Tools
License  : MIT
Requires: curl-bin
Requires: curl-lib
Requires: curl-doc
Requires: ca-certs
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : ca-certs
BuildRequires : cmake
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : groff
BuildRequires : libc6
BuildRequires : libidn-dev
BuildRequires : libidn-dev32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : nghttp2-dev
BuildRequires : nghttp2-dev32
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : pkg-config-dev
BuildRequires : python-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: 0001-Remove-use-of-DES.patch
Patch2: 0002-Add-pacrunner-call-for-autoproxy-resolution.patch
Patch3: 0003-Check-the-state-file-pacdiscovery-sets.patch
Patch4: 0004-Avoid-stripping-the-g-option.patch
Patch5: CVE-2017-1000254.nopatch

%description
_   _ ____  _
___| | | |  _ \| |
/ __| | | | |_) | |
| (__| |_| |  _ <| |___
\___|\___/|_| \_\_____|

%package bin
Summary: bin components for the curl package.
Group: Binaries

%description bin
bin components for the curl package.


%package dev
Summary: dev components for the curl package.
Group: Development
Requires: curl-lib
Requires: curl-bin
Provides: curl-devel

%description dev
dev components for the curl package.


%package dev32
Summary: dev32 components for the curl package.
Group: Default
Requires: curl-lib32
Requires: curl-bin
Requires: curl-dev

%description dev32
dev32 components for the curl package.


%package doc
Summary: doc components for the curl package.
Group: Documentation

%description doc
doc components for the curl package.


%package lib
Summary: lib components for the curl package.
Group: Libraries

%description lib
lib components for the curl package.


%package lib32
Summary: lib32 components for the curl package.
Group: Default

%description lib32
lib32 components for the curl package.


%prep
%setup -q -n curl-7.59.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a curl-7.59.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526008960
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static --with-ssl=/usr \
--disable-ldap \
--without-winidn \
--with-libidn \
--enable-threaded-resolver \
--with-zlib \
--enable-symbol-hiding \
--with-ca-path=/var/cache/ca-certs/anchors \
--disable-ntlm-wb \
--disable-smb \
--enable-proxy \
--with-nghttp2 \
--enable-ipv6 \
--disable-telnet \
--disable-tftp \
--disable-pop3 \
--disable-gopher --with-gssapi=/usr
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --with-ssl=/usr \
--disable-ldap \
--without-winidn \
--with-libidn \
--enable-threaded-resolver \
--with-zlib \
--enable-symbol-hiding \
--with-ca-path=/var/cache/ca-certs/anchors \
--disable-ntlm-wb \
--disable-smb \
--enable-proxy \
--with-nghttp2 \
--enable-ipv6 \
--disable-telnet \
--disable-tftp \
--disable-pop3 \
--disable-gopher  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1526008960
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/curl
/usr/bin/curl-config

%files dev
%defattr(-,root,root,-)
/usr/include/curl/curl.h
/usr/include/curl/curlver.h
/usr/include/curl/easy.h
/usr/include/curl/mprintf.h
/usr/include/curl/multi.h
/usr/include/curl/stdcheaders.h
/usr/include/curl/system.h
/usr/include/curl/typecheck-gcc.h
/usr/lib64/libcurl.so
/usr/lib64/pkgconfig/libcurl.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcurl.so
/usr/lib32/pkgconfig/32libcurl.pc
/usr/lib32/pkgconfig/libcurl.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcurl.so.4
/usr/lib64/libcurl.so.4.5.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcurl.so.4
/usr/lib32/libcurl.so.4.5.0
