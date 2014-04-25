%define upstream_name    HTML-FormFu
%define upstream_version 2.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	HTML Form Management Framework for Perl

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Test::Aggregate::Nested)
BuildRequires: perl(File::ShareDir::Install)
BuildRequires:	perl(CGI)
BuildRequires:	perl(Captcha::reCAPTCHA) >= 0.93
BuildRequires:	perl(Class::Accessor::Chained::Fast)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(Clone) >= 0.31
BuildRequires:	perl(Config::Any) >= 0.18
BuildRequires:	perl(Crypt::CBC)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(Data::Visitor::Callback)
BuildRequires:	perl(Date::Calc)
BuildRequires:	perl(DateTime) >= 0.54
BuildRequires:	perl(DateTime::Format::Builder) >= 0.790.1
BuildRequires:	perl(DateTime::Format::Natural)
BuildRequires:	perl(DateTime::Format::Strptime) >= 1.200.0
BuildRequires:	perl(DateTime::Locale) >= 0.45
BuildRequires:	perl(Email::Valid)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(HTML::Scrubber)
BuildRequires:	perl(HTML::TokeParser::Simple) >= 3.14
BuildRequires:	perl(HTTP::Headers) >= 1.64
BuildRequires:	perl(Hash::Flatten)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Locale::Maketext)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(MooseX::Aliases)
BuildRequires:	perl(MooseX::SetOnce)
BuildRequires:	perl(MooseX::ChainedAccessors::Accessor)
BuildRequires:	perl(Number::Format)
BuildRequires:	perl(Path::Class::File)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::More) >= 0.92
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(YAML::XS)
BuildRequires:	perl(boolean)

BuildArch:	noarch

%description
HTML::FormFu is a HTML form framework which aims to be as easy
as possible to use for basic web forms, but with the power and flexibility
to do anything else you might want to do (as long as it involves forms).

You can configure almost any part of formfu's behaviour and output. By
default formfu renders "XHTML 1.0 Strict" compliant markup, with as little
extra markup as possible, but with sufficient CSS class names to allow for
a wide-range of output styles to be generated by changing only the CSS.

All methods listed below (except the /new manpage) can either be called as
a normal method on your '$form' object, or as an option in your config
file. Examples will mainly be shown in the YAML manpage config syntax.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{perl_vendorlib}/*
%{_bindir}/html_formfu_deploy.pl
%{_bindir}/html_formfu_dumpconf.pl
%{_mandir}/man1/*
%{_mandir}/man3/*


