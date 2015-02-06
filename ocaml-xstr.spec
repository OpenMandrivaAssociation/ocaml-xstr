%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Thread-safe implementation of string searching/matching/splitting
Name:		ocaml-xstr
Version:	0.2.1
Release:	4
License:	MIT/X11
Group:		Development/Other
Url:		http://projects.camlcity.org/projects/xstr.html
Source0:	http://download.camlcity.org/download/xstr-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
This package implements frequent string operations: searching, replacing,
splitting, matching. It is independent from the Str library, and can
replace Str in many cases. Unlike Str, xstr is thread-safe. xstr does
not implement regular expressions in general, but an important subset.
Some operations of xstr are performed as quickly as by Str; if the string
to be processed is small, xstr is often faster than Str; if the string is
big, xstr is upto half as fast than Str.

%files
%doc LICENSE README
%dir %{_libdir}/ocaml/xstr
%{_libdir}/ocaml/xstr/META
%{_libdir}/ocaml/xstr/*.cma
%{_libdir}/ocaml/xstr/*.cmi

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%{_libdir}/ocaml/xstr/*.a
%{_libdir}/ocaml/xstr/*.cmxa
%{_libdir}/ocaml/xstr/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n xstr

%build
make all opt

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/xstr
make install

