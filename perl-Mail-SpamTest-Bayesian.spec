#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	SpamTest-Bayesian
Summary:	Mail::SpamTest::Bayesian - Perl extension for Bayesian spam-testing
Summary(pl):	Mail::SpamTest::Bayesian - rozszerzenie do wykrywania spamu metod± bayesowsk±
Name:		perl-Mail-SpamTest-Bayesian
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(MIME::Parser) >= 5.406
BuildRequires:	perl-BerkeleyDB >= 0.17
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the Bayesian spam-testing algorithm described
by Paul Graham at <http://www.paulgraham.com/spam.html>.

In short: the system is trained by exposure to mailboxes of known spam
and non-spam messages.  These are (1) MIME-decoded, and non-text parts
deleted; (2) tokenised.  The database files spam.db and nonspam.db
contain lists of tokens and the number of messages in which they have
occurred; general.db holds a message count.

%description -l pl
Ten modu³ jest implementacj± bayesowskiego algorytmu wykrywania spamu
opisanego przez Paula Grahama w <http://www.paulgraham.com/spam.html>.

W skrócie: system jest uczony poprzez przedstawianie skrzynek z
wiadomo¶ciami, o których wiadomo, ¿e zawieraj± spam lub go nie
zawieraj±. S± one (1) zakodowane MIME, z usuniêtymi czê¶ciami
nietekstowymi; (2) ztokenizowane. Pliki baz danych spam.db i
nonspam.db zawieraj± listy tokenów i liczby wiadomo¶ci, w których
wyst±pi³y; general.db przechowuje liczbê wiadomo¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_sitelib}/Mail/SpamTest
%{perl_sitelib}/Mail/SpamTest/*.pm
%{_mandir}/man3/*
