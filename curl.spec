#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : curl
Version  : 7.76.0
Release  : 109
URL      : https://github.com/curl/curl/releases/download/curl-7_76_0/curl-7.76.0.tar.xz
Source0  : https://github.com/curl/curl/releases/download/curl-7_76_0/curl-7.76.0.tar.xz
Source1  : https://github.com/curl/curl/releases/download/curl-7_76_0/curl-7.76.0.tar.xz.asc
Summary  : Command line tool and library for transferring data with URLs
Group    : Development/Tools
License  : MIT
Requires: curl-bin = %{version}-%{release}
Requires: curl-lib = %{version}-%{release}
Requires: curl-license = %{version}-%{release}
Requires: curl-man = %{version}-%{release}
Requires: ca-certs
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : ca-certs
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
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zstd-dev
Patch1: 0001-Remove-use-of-DES.patch
Patch2: 0002-Add-pacrunner-call-for-autoproxy-resolution.patch
Patch3: 0003-Check-the-state-file-pacdiscovery-sets.patch
Patch4: 0004-Avoid-stripping-the-g-option.patch
Patch5: 0005-Open-library-file-descriptors-with-O_CLOEXEC.patch

%description
curl is used in command lines or scripts to transfer data. It is also used in
cars, television sets, routers, printers, audio equipment, mobile phones,
tablets, settop boxes, media players and is the internet transfer backbone for
thousands of software applications affecting billions of humans daily.

%package bin
Summary: bin components for the curl package.
Group: Binaries
Requires: curl-license = %{version}-%{release}

%description bin
bin components for the curl package.


%package dev
Summary: dev components for the curl package.
Group: Development
Requires: curl-lib = %{version}-%{release}
Requires: curl-bin = %{version}-%{release}
Provides: curl-devel = %{version}-%{release}
Requires: curl = %{version}-%{release}

%description dev
dev components for the curl package.


%package dev32
Summary: dev32 components for the curl package.
Group: Default
Requires: curl-lib32 = %{version}-%{release}
Requires: curl-bin = %{version}-%{release}
Requires: curl-dev = %{version}-%{release}

%description dev32
dev32 components for the curl package.


%package lib
Summary: lib components for the curl package.
Group: Libraries
Requires: curl-license = %{version}-%{release}

%description lib
lib components for the curl package.


%package lib32
Summary: lib32 components for the curl package.
Group: Default
Requires: curl-license = %{version}-%{release}

%description lib32
lib32 components for the curl package.


%package license
Summary: license components for the curl package.
Group: Default

%description license
license components for the curl package.


%package man
Summary: man components for the curl package.
Group: Default

%description man
man components for the curl package.


%prep
%setup -q -n curl-7.76.0
cd %{_builddir}/curl-7.76.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a curl-7.76.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617338292
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
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
--disable-gopher \
--enable-negotiate --with-gssapi=/usr
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
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
--disable-gopher \
--enable-negotiate  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1617338292
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/curl
cp %{_builddir}/curl-7.76.0/COPYING %{buildroot}/usr/share/package-licenses/curl/73bcd04aed1c45b611fd34aaa29e72069a49049b
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
/usr/include/curl/options.h
/usr/include/curl/stdcheaders.h
/usr/include/curl/system.h
/usr/include/curl/typecheck-gcc.h
/usr/include/curl/urlapi.h
/usr/lib64/libcurl.so
/usr/lib64/pkgconfig/libcurl.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/CURLINFO_ACTIVESOCKET.3
/usr/share/man/man3/CURLINFO_APPCONNECT_TIME.3
/usr/share/man/man3/CURLINFO_APPCONNECT_TIME_T.3
/usr/share/man/man3/CURLINFO_CERTINFO.3
/usr/share/man/man3/CURLINFO_CONDITION_UNMET.3
/usr/share/man/man3/CURLINFO_CONNECT_TIME.3
/usr/share/man/man3/CURLINFO_CONNECT_TIME_T.3
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_DOWNLOAD.3
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_DOWNLOAD_T.3
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_UPLOAD.3
/usr/share/man/man3/CURLINFO_CONTENT_LENGTH_UPLOAD_T.3
/usr/share/man/man3/CURLINFO_CONTENT_TYPE.3
/usr/share/man/man3/CURLINFO_COOKIELIST.3
/usr/share/man/man3/CURLINFO_EFFECTIVE_METHOD.3
/usr/share/man/man3/CURLINFO_EFFECTIVE_URL.3
/usr/share/man/man3/CURLINFO_FILETIME.3
/usr/share/man/man3/CURLINFO_FILETIME_T.3
/usr/share/man/man3/CURLINFO_FTP_ENTRY_PATH.3
/usr/share/man/man3/CURLINFO_HEADER_SIZE.3
/usr/share/man/man3/CURLINFO_HTTPAUTH_AVAIL.3
/usr/share/man/man3/CURLINFO_HTTP_CONNECTCODE.3
/usr/share/man/man3/CURLINFO_HTTP_VERSION.3
/usr/share/man/man3/CURLINFO_LASTSOCKET.3
/usr/share/man/man3/CURLINFO_LOCAL_IP.3
/usr/share/man/man3/CURLINFO_LOCAL_PORT.3
/usr/share/man/man3/CURLINFO_NAMELOOKUP_TIME.3
/usr/share/man/man3/CURLINFO_NAMELOOKUP_TIME_T.3
/usr/share/man/man3/CURLINFO_NUM_CONNECTS.3
/usr/share/man/man3/CURLINFO_OS_ERRNO.3
/usr/share/man/man3/CURLINFO_PRETRANSFER_TIME.3
/usr/share/man/man3/CURLINFO_PRETRANSFER_TIME_T.3
/usr/share/man/man3/CURLINFO_PRIMARY_IP.3
/usr/share/man/man3/CURLINFO_PRIMARY_PORT.3
/usr/share/man/man3/CURLINFO_PRIVATE.3
/usr/share/man/man3/CURLINFO_PROTOCOL.3
/usr/share/man/man3/CURLINFO_PROXYAUTH_AVAIL.3
/usr/share/man/man3/CURLINFO_PROXY_ERROR.3
/usr/share/man/man3/CURLINFO_PROXY_SSL_VERIFYRESULT.3
/usr/share/man/man3/CURLINFO_REDIRECT_COUNT.3
/usr/share/man/man3/CURLINFO_REDIRECT_TIME.3
/usr/share/man/man3/CURLINFO_REDIRECT_TIME_T.3
/usr/share/man/man3/CURLINFO_REDIRECT_URL.3
/usr/share/man/man3/CURLINFO_REFERER.3
/usr/share/man/man3/CURLINFO_REQUEST_SIZE.3
/usr/share/man/man3/CURLINFO_RESPONSE_CODE.3
/usr/share/man/man3/CURLINFO_RETRY_AFTER.3
/usr/share/man/man3/CURLINFO_RTSP_CLIENT_CSEQ.3
/usr/share/man/man3/CURLINFO_RTSP_CSEQ_RECV.3
/usr/share/man/man3/CURLINFO_RTSP_SERVER_CSEQ.3
/usr/share/man/man3/CURLINFO_RTSP_SESSION_ID.3
/usr/share/man/man3/CURLINFO_SCHEME.3
/usr/share/man/man3/CURLINFO_SIZE_DOWNLOAD.3
/usr/share/man/man3/CURLINFO_SIZE_DOWNLOAD_T.3
/usr/share/man/man3/CURLINFO_SIZE_UPLOAD.3
/usr/share/man/man3/CURLINFO_SIZE_UPLOAD_T.3
/usr/share/man/man3/CURLINFO_SPEED_DOWNLOAD.3
/usr/share/man/man3/CURLINFO_SPEED_DOWNLOAD_T.3
/usr/share/man/man3/CURLINFO_SPEED_UPLOAD.3
/usr/share/man/man3/CURLINFO_SPEED_UPLOAD_T.3
/usr/share/man/man3/CURLINFO_SSL_ENGINES.3
/usr/share/man/man3/CURLINFO_SSL_VERIFYRESULT.3
/usr/share/man/man3/CURLINFO_STARTTRANSFER_TIME.3
/usr/share/man/man3/CURLINFO_STARTTRANSFER_TIME_T.3
/usr/share/man/man3/CURLINFO_TLS_SESSION.3
/usr/share/man/man3/CURLINFO_TLS_SSL_PTR.3
/usr/share/man/man3/CURLINFO_TOTAL_TIME.3
/usr/share/man/man3/CURLINFO_TOTAL_TIME_T.3
/usr/share/man/man3/CURLMOPT_CHUNK_LENGTH_PENALTY_SIZE.3
/usr/share/man/man3/CURLMOPT_CONTENT_LENGTH_PENALTY_SIZE.3
/usr/share/man/man3/CURLMOPT_MAXCONNECTS.3
/usr/share/man/man3/CURLMOPT_MAX_CONCURRENT_STREAMS.3
/usr/share/man/man3/CURLMOPT_MAX_HOST_CONNECTIONS.3
/usr/share/man/man3/CURLMOPT_MAX_PIPELINE_LENGTH.3
/usr/share/man/man3/CURLMOPT_MAX_TOTAL_CONNECTIONS.3
/usr/share/man/man3/CURLMOPT_PIPELINING.3
/usr/share/man/man3/CURLMOPT_PIPELINING_SERVER_BL.3
/usr/share/man/man3/CURLMOPT_PIPELINING_SITE_BL.3
/usr/share/man/man3/CURLMOPT_PUSHDATA.3
/usr/share/man/man3/CURLMOPT_PUSHFUNCTION.3
/usr/share/man/man3/CURLMOPT_SOCKETDATA.3
/usr/share/man/man3/CURLMOPT_SOCKETFUNCTION.3
/usr/share/man/man3/CURLMOPT_TIMERDATA.3
/usr/share/man/man3/CURLMOPT_TIMERFUNCTION.3
/usr/share/man/man3/CURLOPT_ABSTRACT_UNIX_SOCKET.3
/usr/share/man/man3/CURLOPT_ACCEPTTIMEOUT_MS.3
/usr/share/man/man3/CURLOPT_ACCEPT_ENCODING.3
/usr/share/man/man3/CURLOPT_ADDRESS_SCOPE.3
/usr/share/man/man3/CURLOPT_ALTSVC.3
/usr/share/man/man3/CURLOPT_ALTSVC_CTRL.3
/usr/share/man/man3/CURLOPT_APPEND.3
/usr/share/man/man3/CURLOPT_AUTOREFERER.3
/usr/share/man/man3/CURLOPT_AWS_SIGV4.3
/usr/share/man/man3/CURLOPT_BUFFERSIZE.3
/usr/share/man/man3/CURLOPT_CAINFO.3
/usr/share/man/man3/CURLOPT_CAPATH.3
/usr/share/man/man3/CURLOPT_CERTINFO.3
/usr/share/man/man3/CURLOPT_CHUNK_BGN_FUNCTION.3
/usr/share/man/man3/CURLOPT_CHUNK_DATA.3
/usr/share/man/man3/CURLOPT_CHUNK_END_FUNCTION.3
/usr/share/man/man3/CURLOPT_CLOSESOCKETDATA.3
/usr/share/man/man3/CURLOPT_CLOSESOCKETFUNCTION.3
/usr/share/man/man3/CURLOPT_CONNECTTIMEOUT.3
/usr/share/man/man3/CURLOPT_CONNECTTIMEOUT_MS.3
/usr/share/man/man3/CURLOPT_CONNECT_ONLY.3
/usr/share/man/man3/CURLOPT_CONNECT_TO.3
/usr/share/man/man3/CURLOPT_CONV_FROM_NETWORK_FUNCTION.3
/usr/share/man/man3/CURLOPT_CONV_FROM_UTF8_FUNCTION.3
/usr/share/man/man3/CURLOPT_CONV_TO_NETWORK_FUNCTION.3
/usr/share/man/man3/CURLOPT_COOKIE.3
/usr/share/man/man3/CURLOPT_COOKIEFILE.3
/usr/share/man/man3/CURLOPT_COOKIEJAR.3
/usr/share/man/man3/CURLOPT_COOKIELIST.3
/usr/share/man/man3/CURLOPT_COOKIESESSION.3
/usr/share/man/man3/CURLOPT_COPYPOSTFIELDS.3
/usr/share/man/man3/CURLOPT_CRLF.3
/usr/share/man/man3/CURLOPT_CRLFILE.3
/usr/share/man/man3/CURLOPT_CURLU.3
/usr/share/man/man3/CURLOPT_CUSTOMREQUEST.3
/usr/share/man/man3/CURLOPT_DEBUGDATA.3
/usr/share/man/man3/CURLOPT_DEBUGFUNCTION.3
/usr/share/man/man3/CURLOPT_DEFAULT_PROTOCOL.3
/usr/share/man/man3/CURLOPT_DIRLISTONLY.3
/usr/share/man/man3/CURLOPT_DISALLOW_USERNAME_IN_URL.3
/usr/share/man/man3/CURLOPT_DNS_CACHE_TIMEOUT.3
/usr/share/man/man3/CURLOPT_DNS_INTERFACE.3
/usr/share/man/man3/CURLOPT_DNS_LOCAL_IP4.3
/usr/share/man/man3/CURLOPT_DNS_LOCAL_IP6.3
/usr/share/man/man3/CURLOPT_DNS_SERVERS.3
/usr/share/man/man3/CURLOPT_DNS_SHUFFLE_ADDRESSES.3
/usr/share/man/man3/CURLOPT_DNS_USE_GLOBAL_CACHE.3
/usr/share/man/man3/CURLOPT_DOH_SSL_VERIFYHOST.3
/usr/share/man/man3/CURLOPT_DOH_SSL_VERIFYPEER.3
/usr/share/man/man3/CURLOPT_DOH_SSL_VERIFYSTATUS.3
/usr/share/man/man3/CURLOPT_DOH_URL.3
/usr/share/man/man3/CURLOPT_EGDSOCKET.3
/usr/share/man/man3/CURLOPT_ERRORBUFFER.3
/usr/share/man/man3/CURLOPT_EXPECT_100_TIMEOUT_MS.3
/usr/share/man/man3/CURLOPT_FAILONERROR.3
/usr/share/man/man3/CURLOPT_FILETIME.3
/usr/share/man/man3/CURLOPT_FNMATCH_DATA.3
/usr/share/man/man3/CURLOPT_FNMATCH_FUNCTION.3
/usr/share/man/man3/CURLOPT_FOLLOWLOCATION.3
/usr/share/man/man3/CURLOPT_FORBID_REUSE.3
/usr/share/man/man3/CURLOPT_FRESH_CONNECT.3
/usr/share/man/man3/CURLOPT_FTPPORT.3
/usr/share/man/man3/CURLOPT_FTPSSLAUTH.3
/usr/share/man/man3/CURLOPT_FTP_ACCOUNT.3
/usr/share/man/man3/CURLOPT_FTP_ALTERNATIVE_TO_USER.3
/usr/share/man/man3/CURLOPT_FTP_CREATE_MISSING_DIRS.3
/usr/share/man/man3/CURLOPT_FTP_FILEMETHOD.3
/usr/share/man/man3/CURLOPT_FTP_RESPONSE_TIMEOUT.3
/usr/share/man/man3/CURLOPT_FTP_SKIP_PASV_IP.3
/usr/share/man/man3/CURLOPT_FTP_SSL_CCC.3
/usr/share/man/man3/CURLOPT_FTP_USE_EPRT.3
/usr/share/man/man3/CURLOPT_FTP_USE_EPSV.3
/usr/share/man/man3/CURLOPT_FTP_USE_PRET.3
/usr/share/man/man3/CURLOPT_GSSAPI_DELEGATION.3
/usr/share/man/man3/CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS.3
/usr/share/man/man3/CURLOPT_HAPROXYPROTOCOL.3
/usr/share/man/man3/CURLOPT_HEADER.3
/usr/share/man/man3/CURLOPT_HEADERDATA.3
/usr/share/man/man3/CURLOPT_HEADERFUNCTION.3
/usr/share/man/man3/CURLOPT_HEADEROPT.3
/usr/share/man/man3/CURLOPT_HSTS.3
/usr/share/man/man3/CURLOPT_HSTSREADDATA.3
/usr/share/man/man3/CURLOPT_HSTSREADFUNCTION.3
/usr/share/man/man3/CURLOPT_HSTSWRITEDATA.3
/usr/share/man/man3/CURLOPT_HSTSWRITEFUNCTION.3
/usr/share/man/man3/CURLOPT_HSTS_CTRL.3
/usr/share/man/man3/CURLOPT_HTTP09_ALLOWED.3
/usr/share/man/man3/CURLOPT_HTTP200ALIASES.3
/usr/share/man/man3/CURLOPT_HTTPAUTH.3
/usr/share/man/man3/CURLOPT_HTTPGET.3
/usr/share/man/man3/CURLOPT_HTTPHEADER.3
/usr/share/man/man3/CURLOPT_HTTPPOST.3
/usr/share/man/man3/CURLOPT_HTTPPROXYTUNNEL.3
/usr/share/man/man3/CURLOPT_HTTP_CONTENT_DECODING.3
/usr/share/man/man3/CURLOPT_HTTP_TRANSFER_DECODING.3
/usr/share/man/man3/CURLOPT_HTTP_VERSION.3
/usr/share/man/man3/CURLOPT_IGNORE_CONTENT_LENGTH.3
/usr/share/man/man3/CURLOPT_INFILESIZE.3
/usr/share/man/man3/CURLOPT_INFILESIZE_LARGE.3
/usr/share/man/man3/CURLOPT_INTERFACE.3
/usr/share/man/man3/CURLOPT_INTERLEAVEDATA.3
/usr/share/man/man3/CURLOPT_INTERLEAVEFUNCTION.3
/usr/share/man/man3/CURLOPT_IOCTLDATA.3
/usr/share/man/man3/CURLOPT_IOCTLFUNCTION.3
/usr/share/man/man3/CURLOPT_IPRESOLVE.3
/usr/share/man/man3/CURLOPT_ISSUERCERT.3
/usr/share/man/man3/CURLOPT_ISSUERCERT_BLOB.3
/usr/share/man/man3/CURLOPT_KEEP_SENDING_ON_ERROR.3
/usr/share/man/man3/CURLOPT_KEYPASSWD.3
/usr/share/man/man3/CURLOPT_KRBLEVEL.3
/usr/share/man/man3/CURLOPT_LOCALPORT.3
/usr/share/man/man3/CURLOPT_LOCALPORTRANGE.3
/usr/share/man/man3/CURLOPT_LOGIN_OPTIONS.3
/usr/share/man/man3/CURLOPT_LOW_SPEED_LIMIT.3
/usr/share/man/man3/CURLOPT_LOW_SPEED_TIME.3
/usr/share/man/man3/CURLOPT_MAIL_AUTH.3
/usr/share/man/man3/CURLOPT_MAIL_FROM.3
/usr/share/man/man3/CURLOPT_MAIL_RCPT.3
/usr/share/man/man3/CURLOPT_MAIL_RCPT_ALLLOWFAILS.3
/usr/share/man/man3/CURLOPT_MAXAGE_CONN.3
/usr/share/man/man3/CURLOPT_MAXCONNECTS.3
/usr/share/man/man3/CURLOPT_MAXFILESIZE.3
/usr/share/man/man3/CURLOPT_MAXFILESIZE_LARGE.3
/usr/share/man/man3/CURLOPT_MAXREDIRS.3
/usr/share/man/man3/CURLOPT_MAX_RECV_SPEED_LARGE.3
/usr/share/man/man3/CURLOPT_MAX_SEND_SPEED_LARGE.3
/usr/share/man/man3/CURLOPT_MIMEPOST.3
/usr/share/man/man3/CURLOPT_NETRC.3
/usr/share/man/man3/CURLOPT_NETRC_FILE.3
/usr/share/man/man3/CURLOPT_NEW_DIRECTORY_PERMS.3
/usr/share/man/man3/CURLOPT_NEW_FILE_PERMS.3
/usr/share/man/man3/CURLOPT_NOBODY.3
/usr/share/man/man3/CURLOPT_NOPROGRESS.3
/usr/share/man/man3/CURLOPT_NOPROXY.3
/usr/share/man/man3/CURLOPT_NOSIGNAL.3
/usr/share/man/man3/CURLOPT_OPENSOCKETDATA.3
/usr/share/man/man3/CURLOPT_OPENSOCKETFUNCTION.3
/usr/share/man/man3/CURLOPT_PASSWORD.3
/usr/share/man/man3/CURLOPT_PATH_AS_IS.3
/usr/share/man/man3/CURLOPT_PINNEDPUBLICKEY.3
/usr/share/man/man3/CURLOPT_PIPEWAIT.3
/usr/share/man/man3/CURLOPT_PORT.3
/usr/share/man/man3/CURLOPT_POST.3
/usr/share/man/man3/CURLOPT_POSTFIELDS.3
/usr/share/man/man3/CURLOPT_POSTFIELDSIZE.3
/usr/share/man/man3/CURLOPT_POSTFIELDSIZE_LARGE.3
/usr/share/man/man3/CURLOPT_POSTQUOTE.3
/usr/share/man/man3/CURLOPT_POSTREDIR.3
/usr/share/man/man3/CURLOPT_PREQUOTE.3
/usr/share/man/man3/CURLOPT_PRE_PROXY.3
/usr/share/man/man3/CURLOPT_PRIVATE.3
/usr/share/man/man3/CURLOPT_PROGRESSDATA.3
/usr/share/man/man3/CURLOPT_PROGRESSFUNCTION.3
/usr/share/man/man3/CURLOPT_PROTOCOLS.3
/usr/share/man/man3/CURLOPT_PROXY.3
/usr/share/man/man3/CURLOPT_PROXYAUTH.3
/usr/share/man/man3/CURLOPT_PROXYHEADER.3
/usr/share/man/man3/CURLOPT_PROXYPASSWORD.3
/usr/share/man/man3/CURLOPT_PROXYPORT.3
/usr/share/man/man3/CURLOPT_PROXYTYPE.3
/usr/share/man/man3/CURLOPT_PROXYUSERNAME.3
/usr/share/man/man3/CURLOPT_PROXYUSERPWD.3
/usr/share/man/man3/CURLOPT_PROXY_CAINFO.3
/usr/share/man/man3/CURLOPT_PROXY_CAPATH.3
/usr/share/man/man3/CURLOPT_PROXY_CRLFILE.3
/usr/share/man/man3/CURLOPT_PROXY_ISSUERCERT.3
/usr/share/man/man3/CURLOPT_PROXY_ISSUERCERT_BLOB.3
/usr/share/man/man3/CURLOPT_PROXY_KEYPASSWD.3
/usr/share/man/man3/CURLOPT_PROXY_PINNEDPUBLICKEY.3
/usr/share/man/man3/CURLOPT_PROXY_SERVICE_NAME.3
/usr/share/man/man3/CURLOPT_PROXY_SSLCERT.3
/usr/share/man/man3/CURLOPT_PROXY_SSLCERTTYPE.3
/usr/share/man/man3/CURLOPT_PROXY_SSLCERT_BLOB.3
/usr/share/man/man3/CURLOPT_PROXY_SSLKEY.3
/usr/share/man/man3/CURLOPT_PROXY_SSLKEYTYPE.3
/usr/share/man/man3/CURLOPT_PROXY_SSLKEY_BLOB.3
/usr/share/man/man3/CURLOPT_PROXY_SSLVERSION.3
/usr/share/man/man3/CURLOPT_PROXY_SSL_CIPHER_LIST.3
/usr/share/man/man3/CURLOPT_PROXY_SSL_OPTIONS.3
/usr/share/man/man3/CURLOPT_PROXY_SSL_VERIFYHOST.3
/usr/share/man/man3/CURLOPT_PROXY_SSL_VERIFYPEER.3
/usr/share/man/man3/CURLOPT_PROXY_TLS13_CIPHERS.3
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_PASSWORD.3
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_TYPE.3
/usr/share/man/man3/CURLOPT_PROXY_TLSAUTH_USERNAME.3
/usr/share/man/man3/CURLOPT_PROXY_TRANSFER_MODE.3
/usr/share/man/man3/CURLOPT_PUT.3
/usr/share/man/man3/CURLOPT_QUOTE.3
/usr/share/man/man3/CURLOPT_RANDOM_FILE.3
/usr/share/man/man3/CURLOPT_RANGE.3
/usr/share/man/man3/CURLOPT_READDATA.3
/usr/share/man/man3/CURLOPT_READFUNCTION.3
/usr/share/man/man3/CURLOPT_REDIR_PROTOCOLS.3
/usr/share/man/man3/CURLOPT_REFERER.3
/usr/share/man/man3/CURLOPT_REQUEST_TARGET.3
/usr/share/man/man3/CURLOPT_RESOLVE.3
/usr/share/man/man3/CURLOPT_RESOLVER_START_DATA.3
/usr/share/man/man3/CURLOPT_RESOLVER_START_FUNCTION.3
/usr/share/man/man3/CURLOPT_RESUME_FROM.3
/usr/share/man/man3/CURLOPT_RESUME_FROM_LARGE.3
/usr/share/man/man3/CURLOPT_RTSP_CLIENT_CSEQ.3
/usr/share/man/man3/CURLOPT_RTSP_REQUEST.3
/usr/share/man/man3/CURLOPT_RTSP_SERVER_CSEQ.3
/usr/share/man/man3/CURLOPT_RTSP_SESSION_ID.3
/usr/share/man/man3/CURLOPT_RTSP_STREAM_URI.3
/usr/share/man/man3/CURLOPT_RTSP_TRANSPORT.3
/usr/share/man/man3/CURLOPT_SASL_AUTHZID.3
/usr/share/man/man3/CURLOPT_SASL_IR.3
/usr/share/man/man3/CURLOPT_SEEKDATA.3
/usr/share/man/man3/CURLOPT_SEEKFUNCTION.3
/usr/share/man/man3/CURLOPT_SERVICE_NAME.3
/usr/share/man/man3/CURLOPT_SHARE.3
/usr/share/man/man3/CURLOPT_SOCKOPTDATA.3
/usr/share/man/man3/CURLOPT_SOCKOPTFUNCTION.3
/usr/share/man/man3/CURLOPT_SOCKS5_AUTH.3
/usr/share/man/man3/CURLOPT_SOCKS5_GSSAPI_NEC.3
/usr/share/man/man3/CURLOPT_SOCKS5_GSSAPI_SERVICE.3
/usr/share/man/man3/CURLOPT_SSH_AUTH_TYPES.3
/usr/share/man/man3/CURLOPT_SSH_COMPRESSION.3
/usr/share/man/man3/CURLOPT_SSH_HOST_PUBLIC_KEY_MD5.3
/usr/share/man/man3/CURLOPT_SSH_KEYDATA.3
/usr/share/man/man3/CURLOPT_SSH_KEYFUNCTION.3
/usr/share/man/man3/CURLOPT_SSH_KNOWNHOSTS.3
/usr/share/man/man3/CURLOPT_SSH_PRIVATE_KEYFILE.3
/usr/share/man/man3/CURLOPT_SSH_PUBLIC_KEYFILE.3
/usr/share/man/man3/CURLOPT_SSLCERT.3
/usr/share/man/man3/CURLOPT_SSLCERTTYPE.3
/usr/share/man/man3/CURLOPT_SSLCERT_BLOB.3
/usr/share/man/man3/CURLOPT_SSLENGINE.3
/usr/share/man/man3/CURLOPT_SSLENGINE_DEFAULT.3
/usr/share/man/man3/CURLOPT_SSLKEY.3
/usr/share/man/man3/CURLOPT_SSLKEYTYPE.3
/usr/share/man/man3/CURLOPT_SSLKEY_BLOB.3
/usr/share/man/man3/CURLOPT_SSLVERSION.3
/usr/share/man/man3/CURLOPT_SSL_CIPHER_LIST.3
/usr/share/man/man3/CURLOPT_SSL_CTX_DATA.3
/usr/share/man/man3/CURLOPT_SSL_CTX_FUNCTION.3
/usr/share/man/man3/CURLOPT_SSL_EC_CURVES.3
/usr/share/man/man3/CURLOPT_SSL_ENABLE_ALPN.3
/usr/share/man/man3/CURLOPT_SSL_ENABLE_NPN.3
/usr/share/man/man3/CURLOPT_SSL_FALSESTART.3
/usr/share/man/man3/CURLOPT_SSL_OPTIONS.3
/usr/share/man/man3/CURLOPT_SSL_SESSIONID_CACHE.3
/usr/share/man/man3/CURLOPT_SSL_VERIFYHOST.3
/usr/share/man/man3/CURLOPT_SSL_VERIFYPEER.3
/usr/share/man/man3/CURLOPT_SSL_VERIFYSTATUS.3
/usr/share/man/man3/CURLOPT_STDERR.3
/usr/share/man/man3/CURLOPT_STREAM_DEPENDS.3
/usr/share/man/man3/CURLOPT_STREAM_DEPENDS_E.3
/usr/share/man/man3/CURLOPT_STREAM_WEIGHT.3
/usr/share/man/man3/CURLOPT_SUPPRESS_CONNECT_HEADERS.3
/usr/share/man/man3/CURLOPT_TCP_FASTOPEN.3
/usr/share/man/man3/CURLOPT_TCP_KEEPALIVE.3
/usr/share/man/man3/CURLOPT_TCP_KEEPIDLE.3
/usr/share/man/man3/CURLOPT_TCP_KEEPINTVL.3
/usr/share/man/man3/CURLOPT_TCP_NODELAY.3
/usr/share/man/man3/CURLOPT_TELNETOPTIONS.3
/usr/share/man/man3/CURLOPT_TFTP_BLKSIZE.3
/usr/share/man/man3/CURLOPT_TFTP_NO_OPTIONS.3
/usr/share/man/man3/CURLOPT_TIMECONDITION.3
/usr/share/man/man3/CURLOPT_TIMEOUT.3
/usr/share/man/man3/CURLOPT_TIMEOUT_MS.3
/usr/share/man/man3/CURLOPT_TIMEVALUE.3
/usr/share/man/man3/CURLOPT_TIMEVALUE_LARGE.3
/usr/share/man/man3/CURLOPT_TLS13_CIPHERS.3
/usr/share/man/man3/CURLOPT_TLSAUTH_PASSWORD.3
/usr/share/man/man3/CURLOPT_TLSAUTH_TYPE.3
/usr/share/man/man3/CURLOPT_TLSAUTH_USERNAME.3
/usr/share/man/man3/CURLOPT_TRAILERDATA.3
/usr/share/man/man3/CURLOPT_TRAILERFUNCTION.3
/usr/share/man/man3/CURLOPT_TRANSFERTEXT.3
/usr/share/man/man3/CURLOPT_TRANSFER_ENCODING.3
/usr/share/man/man3/CURLOPT_UNIX_SOCKET_PATH.3
/usr/share/man/man3/CURLOPT_UNRESTRICTED_AUTH.3
/usr/share/man/man3/CURLOPT_UPKEEP_INTERVAL_MS.3
/usr/share/man/man3/CURLOPT_UPLOAD.3
/usr/share/man/man3/CURLOPT_UPLOAD_BUFFERSIZE.3
/usr/share/man/man3/CURLOPT_URL.3
/usr/share/man/man3/CURLOPT_USERAGENT.3
/usr/share/man/man3/CURLOPT_USERNAME.3
/usr/share/man/man3/CURLOPT_USERPWD.3
/usr/share/man/man3/CURLOPT_USE_SSL.3
/usr/share/man/man3/CURLOPT_VERBOSE.3
/usr/share/man/man3/CURLOPT_WILDCARDMATCH.3
/usr/share/man/man3/CURLOPT_WRITEDATA.3
/usr/share/man/man3/CURLOPT_WRITEFUNCTION.3
/usr/share/man/man3/CURLOPT_XFERINFODATA.3
/usr/share/man/man3/CURLOPT_XFERINFOFUNCTION.3
/usr/share/man/man3/CURLOPT_XOAUTH2_BEARER.3
/usr/share/man/man3/curl_easy_cleanup.3
/usr/share/man/man3/curl_easy_duphandle.3
/usr/share/man/man3/curl_easy_escape.3
/usr/share/man/man3/curl_easy_getinfo.3
/usr/share/man/man3/curl_easy_init.3
/usr/share/man/man3/curl_easy_option_by_id.3
/usr/share/man/man3/curl_easy_option_by_name.3
/usr/share/man/man3/curl_easy_option_next.3
/usr/share/man/man3/curl_easy_pause.3
/usr/share/man/man3/curl_easy_perform.3
/usr/share/man/man3/curl_easy_recv.3
/usr/share/man/man3/curl_easy_reset.3
/usr/share/man/man3/curl_easy_send.3
/usr/share/man/man3/curl_easy_setopt.3
/usr/share/man/man3/curl_easy_strerror.3
/usr/share/man/man3/curl_easy_unescape.3
/usr/share/man/man3/curl_easy_upkeep.3
/usr/share/man/man3/curl_escape.3
/usr/share/man/man3/curl_formadd.3
/usr/share/man/man3/curl_formfree.3
/usr/share/man/man3/curl_formget.3
/usr/share/man/man3/curl_free.3
/usr/share/man/man3/curl_getdate.3
/usr/share/man/man3/curl_getenv.3
/usr/share/man/man3/curl_global_cleanup.3
/usr/share/man/man3/curl_global_init.3
/usr/share/man/man3/curl_global_init_mem.3
/usr/share/man/man3/curl_global_sslset.3
/usr/share/man/man3/curl_mime_addpart.3
/usr/share/man/man3/curl_mime_data.3
/usr/share/man/man3/curl_mime_data_cb.3
/usr/share/man/man3/curl_mime_encoder.3
/usr/share/man/man3/curl_mime_filedata.3
/usr/share/man/man3/curl_mime_filename.3
/usr/share/man/man3/curl_mime_free.3
/usr/share/man/man3/curl_mime_headers.3
/usr/share/man/man3/curl_mime_init.3
/usr/share/man/man3/curl_mime_name.3
/usr/share/man/man3/curl_mime_subparts.3
/usr/share/man/man3/curl_mime_type.3
/usr/share/man/man3/curl_mprintf.3
/usr/share/man/man3/curl_multi_add_handle.3
/usr/share/man/man3/curl_multi_assign.3
/usr/share/man/man3/curl_multi_cleanup.3
/usr/share/man/man3/curl_multi_fdset.3
/usr/share/man/man3/curl_multi_info_read.3
/usr/share/man/man3/curl_multi_init.3
/usr/share/man/man3/curl_multi_perform.3
/usr/share/man/man3/curl_multi_poll.3
/usr/share/man/man3/curl_multi_remove_handle.3
/usr/share/man/man3/curl_multi_setopt.3
/usr/share/man/man3/curl_multi_socket.3
/usr/share/man/man3/curl_multi_socket_action.3
/usr/share/man/man3/curl_multi_socket_all.3
/usr/share/man/man3/curl_multi_strerror.3
/usr/share/man/man3/curl_multi_timeout.3
/usr/share/man/man3/curl_multi_wait.3
/usr/share/man/man3/curl_multi_wakeup.3
/usr/share/man/man3/curl_share_cleanup.3
/usr/share/man/man3/curl_share_init.3
/usr/share/man/man3/curl_share_setopt.3
/usr/share/man/man3/curl_share_strerror.3
/usr/share/man/man3/curl_slist_append.3
/usr/share/man/man3/curl_slist_free_all.3
/usr/share/man/man3/curl_strequal.3
/usr/share/man/man3/curl_strnequal.3
/usr/share/man/man3/curl_unescape.3
/usr/share/man/man3/curl_url.3
/usr/share/man/man3/curl_url_cleanup.3
/usr/share/man/man3/curl_url_dup.3
/usr/share/man/man3/curl_url_get.3
/usr/share/man/man3/curl_url_set.3
/usr/share/man/man3/curl_version.3
/usr/share/man/man3/curl_version_info.3
/usr/share/man/man3/libcurl-easy.3
/usr/share/man/man3/libcurl-env.3
/usr/share/man/man3/libcurl-errors.3
/usr/share/man/man3/libcurl-multi.3
/usr/share/man/man3/libcurl-security.3
/usr/share/man/man3/libcurl-share.3
/usr/share/man/man3/libcurl-symbols.3
/usr/share/man/man3/libcurl-thread.3
/usr/share/man/man3/libcurl-tutorial.3
/usr/share/man/man3/libcurl-url.3
/usr/share/man/man3/libcurl.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcurl.so
/usr/lib32/pkgconfig/32libcurl.pc
/usr/lib32/pkgconfig/libcurl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcurl.so.4
/usr/lib64/libcurl.so.4.7.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcurl.so.4
/usr/lib32/libcurl.so.4.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/curl/73bcd04aed1c45b611fd34aaa29e72069a49049b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/curl-config.1
/usr/share/man/man1/curl.1
