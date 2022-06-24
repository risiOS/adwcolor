Name:           adwcolor
Version:        1.0
Release:        1%{?dist}
Summary:        Easily modify and create Libadwaita color themes

License:        GPL v3
URL:            https://github.com/risiOS/adwcolor
Source0:        https://github.com/risiOS/adwcolor/archive/refs/heads/main.tar.gz

BuildArch:	noarch

BuildRequires:  python3-devel
Requires: 		python3.10
Recommends:		adw-gtk-theme

%description
Easily Modify and create Libadwaita color themes by modifying the ~/.config/gtk-4.0/gtk.css.

%prep
%autosetup -n %{name}-main

%build
%install
mkdir -p %{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}%{_bindir}

install -m 0755 *.py %{buildroot}%{python3_sitelib}/adwcolor
install -m 0755 risi-script-run.py %{buildroot}%{_bindir}/risi-script-run
cp io.risi.script.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas
cp application-x-risisc.xml %{buildroot}%{_datadir}/mime/packages/application-x-risisc.xml

install -m 0755 risi-script-gtk/__main__.py %{buildroot}%{_bindir}/risi-script-gtk
cp risi-script-gtk/risi-script-gtk.ui %{buildroot}%{_datadir}/risi-script-gtk/risi-script-gtk.ui
cp risi-script-gtk/risi-script-gtk.desktop %{buildroot}%{_datadir}/applications

%files
# %license add-license-file-here
# %doc add-docs-here
%dir %{python3_sitelib}/adwcolor
%{_bindir}/adwcolor
%license LICENSE

%changelog
* Fri Jun 24 2022 PizzaLovingNerd
- First spec file
