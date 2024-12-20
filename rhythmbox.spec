#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: 5424026
#
Name     : rhythmbox
Version  : 3.4.8
Release  : 14
URL      : https://download.gnome.org/sources/rhythmbox/3.4/rhythmbox-3.4.8.tar.xz
Source0  : https://download.gnome.org/sources/rhythmbox/3.4/rhythmbox-3.4.8.tar.xz
Summary  : plugin API for rhythmbox
Group    : Development/Tools
License  : GPL-2.0
Requires: rhythmbox-bin = %{version}-%{release}
Requires: rhythmbox-data = %{version}-%{release}
Requires: rhythmbox-lib = %{version}-%{release}
Requires: rhythmbox-libexec = %{version}-%{release}
Requires: rhythmbox-license = %{version}-%{release}
Requires: rhythmbox-locales = %{version}-%{release}
Requires: rhythmbox-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : clutter-dev
BuildRequires : clutter-gst-dev
BuildRequires : gdk-pixbuf
BuildRequires : gst-plugins-base-dev
BuildRequires : libnotify-dev
BuildRequires : libpeas-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(grilo-0.3)
BuildRequires : pkgconfig(libmtp)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpeas-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(tdb)
BuildRequires : pkgconfig(totem-plparser)
BuildRequires : pygobject
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Rhythmbox
Rhythmbox is your one-stop multimedia application, supporting
a music library, multiple playlists, internet radio, and more.

%package bin
Summary: bin components for the rhythmbox package.
Group: Binaries
Requires: rhythmbox-data = %{version}-%{release}
Requires: rhythmbox-libexec = %{version}-%{release}
Requires: rhythmbox-license = %{version}-%{release}

%description bin
bin components for the rhythmbox package.


%package data
Summary: data components for the rhythmbox package.
Group: Data

%description data
data components for the rhythmbox package.


%package dev
Summary: dev components for the rhythmbox package.
Group: Development
Requires: rhythmbox-lib = %{version}-%{release}
Requires: rhythmbox-bin = %{version}-%{release}
Requires: rhythmbox-data = %{version}-%{release}
Provides: rhythmbox-devel = %{version}-%{release}
Requires: rhythmbox = %{version}-%{release}

%description dev
dev components for the rhythmbox package.


%package doc
Summary: doc components for the rhythmbox package.
Group: Documentation
Requires: rhythmbox-man = %{version}-%{release}

%description doc
doc components for the rhythmbox package.


%package lib
Summary: lib components for the rhythmbox package.
Group: Libraries
Requires: rhythmbox-data = %{version}-%{release}
Requires: rhythmbox-libexec = %{version}-%{release}
Requires: rhythmbox-license = %{version}-%{release}

%description lib
lib components for the rhythmbox package.


%package libexec
Summary: libexec components for the rhythmbox package.
Group: Default
Requires: rhythmbox-license = %{version}-%{release}

%description libexec
libexec components for the rhythmbox package.


%package license
Summary: license components for the rhythmbox package.
Group: Default

%description license
license components for the rhythmbox package.


%package locales
Summary: locales components for the rhythmbox package.
Group: Default

%description locales
locales components for the rhythmbox package.


%package man
Summary: man components for the rhythmbox package.
Group: Default

%description man
man components for the rhythmbox package.


%prep
%setup -q -n rhythmbox-3.4.8
cd %{_builddir}/rhythmbox-3.4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732304251
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/rhythmbox
cp %{_builddir}/rhythmbox-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rhythmbox/3f772bdc589b117aeeb6fbbf5bd277d7c3015a56 || :
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang rhythmbox

%files
%defattr(-,root,root,-)
/usr/lib64/rhythmbox/plugins/android/android.plugin
/usr/lib64/rhythmbox/plugins/artsearch/artsearch.plugin
/usr/lib64/rhythmbox/plugins/artsearch/artsearch.py
/usr/lib64/rhythmbox/plugins/artsearch/embedded.py
/usr/lib64/rhythmbox/plugins/artsearch/lastfm.py
/usr/lib64/rhythmbox/plugins/artsearch/local.py
/usr/lib64/rhythmbox/plugins/artsearch/musicbrainz.py
/usr/lib64/rhythmbox/plugins/artsearch/oldcache.py
/usr/lib64/rhythmbox/plugins/artsearch/songinfo.py
/usr/lib64/rhythmbox/plugins/audiocd/audiocd.plugin
/usr/lib64/rhythmbox/plugins/audioscrobbler/audioscrobbler.plugin
/usr/lib64/rhythmbox/plugins/dbus-media-server/dbus-media-server.plugin
/usr/lib64/rhythmbox/plugins/fmradio/fmradio.plugin
/usr/lib64/rhythmbox/plugins/generic-player/generic-player.plugin
/usr/lib64/rhythmbox/plugins/grilo/grilo.plugin
/usr/lib64/rhythmbox/plugins/im-status/im-status.plugin
/usr/lib64/rhythmbox/plugins/im-status/im-status.py
/usr/lib64/rhythmbox/plugins/iradio/iradio.plugin
/usr/lib64/rhythmbox/plugins/listenbrainz/client.py
/usr/lib64/rhythmbox/plugins/listenbrainz/listenbrainz.plugin
/usr/lib64/rhythmbox/plugins/listenbrainz/listenbrainz.py
/usr/lib64/rhythmbox/plugins/listenbrainz/queue.py
/usr/lib64/rhythmbox/plugins/listenbrainz/settings.py
/usr/lib64/rhythmbox/plugins/lyrics/AstrawebParser.py
/usr/lib64/rhythmbox/plugins/lyrics/DarkLyricsParser.py
/usr/lib64/rhythmbox/plugins/lyrics/JetlyricsParser.py
/usr/lib64/rhythmbox/plugins/lyrics/JlyricParser.py
/usr/lib64/rhythmbox/plugins/lyrics/LyricWikiParser.py
/usr/lib64/rhythmbox/plugins/lyrics/LyricsConfigureDialog.py
/usr/lib64/rhythmbox/plugins/lyrics/LyricsParse.py
/usr/lib64/rhythmbox/plugins/lyrics/LyricsSites.py
/usr/lib64/rhythmbox/plugins/lyrics/TerraParser.py
/usr/lib64/rhythmbox/plugins/lyrics/WinampcnParser.py
/usr/lib64/rhythmbox/plugins/lyrics/lyrics.plugin
/usr/lib64/rhythmbox/plugins/lyrics/lyrics.py
/usr/lib64/rhythmbox/plugins/magnatune/DownloadAlbumHandler.py
/usr/lib64/rhythmbox/plugins/magnatune/MagnatuneAccount.py
/usr/lib64/rhythmbox/plugins/magnatune/MagnatuneSource.py
/usr/lib64/rhythmbox/plugins/magnatune/TrackListHandler.py
/usr/lib64/rhythmbox/plugins/magnatune/magnatune.plugin
/usr/lib64/rhythmbox/plugins/magnatune/magnatune.py
/usr/lib64/rhythmbox/plugins/mpris/mpris.plugin
/usr/lib64/rhythmbox/plugins/mtpdevice/mtpdevice.plugin
/usr/lib64/rhythmbox/plugins/notification/notification.plugin
/usr/lib64/rhythmbox/plugins/power-manager/power-manager.plugin
/usr/lib64/rhythmbox/plugins/python-console/pythonconsole.plugin
/usr/lib64/rhythmbox/plugins/python-console/pythonconsole.py
/usr/lib64/rhythmbox/plugins/rb/Coroutine.py
/usr/lib64/rhythmbox/plugins/rb/Loader.py
/usr/lib64/rhythmbox/plugins/rb/URLCache.py
/usr/lib64/rhythmbox/plugins/rb/rb.plugin
/usr/lib64/rhythmbox/plugins/rb/rb.py
/usr/lib64/rhythmbox/plugins/rb/rbconfig.py
/usr/lib64/rhythmbox/plugins/rb/stringmatch.py
/usr/lib64/rhythmbox/plugins/rbzeitgeist/rbzeitgeist.plugin
/usr/lib64/rhythmbox/plugins/rbzeitgeist/rbzeitgeist.py
/usr/lib64/rhythmbox/plugins/replaygain/config.py
/usr/lib64/rhythmbox/plugins/replaygain/player.py
/usr/lib64/rhythmbox/plugins/replaygain/replaygain.plugin
/usr/lib64/rhythmbox/plugins/replaygain/replaygain.py
/usr/lib64/rhythmbox/plugins/webremote/siphash.py
/usr/lib64/rhythmbox/plugins/webremote/webremote.plugin
/usr/lib64/rhythmbox/plugins/webremote/webremote.py

%files bin
%defattr(-,root,root,-)
/usr/bin/rhythmbox
/usr/bin/rhythmbox-client

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/MPID-3.0.typelib
/usr/lib64/girepository-1.0/RB-3.0.typelib
/usr/share/applications/org.gnome.Rhythmbox3.desktop
/usr/share/applications/org.gnome.Rhythmbox3.device.desktop
/usr/share/dbus-1/services/org.gnome.Rhythmbox3.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3.svg
/usr/share/metainfo/org.gnome.Rhythmbox3.appdata.xml
/usr/share/rhythmbox/plugins/audioscrobbler/audioscrobbler-preferences.ui
/usr/share/rhythmbox/plugins/audioscrobbler/audioscrobbler-profile.ui
/usr/share/rhythmbox/plugins/audioscrobbler/icons/hicolor/scalable/places/Last.fm-symbolic.svg
/usr/share/rhythmbox/plugins/listenbrainz/settings.ui
/usr/share/rhythmbox/plugins/lyrics/lyrics-prefs.ui
/usr/share/rhythmbox/plugins/magnatune/icons/hicolor/scalable/places/magnatune-symbolic.svg
/usr/share/rhythmbox/plugins/magnatune/magnatune-loading.ui
/usr/share/rhythmbox/plugins/magnatune/magnatune-popup.ui
/usr/share/rhythmbox/plugins/magnatune/magnatune-prefs.ui
/usr/share/rhythmbox/plugins/magnatune/magnatune-toolbar.ui
/usr/share/rhythmbox/plugins/magnatune/magnatune_logo_color_small.png
/usr/share/rhythmbox/plugins/magnatune/magnatune_logo_color_tiny.png
/usr/share/rhythmbox/plugins/replaygain/replaygain-prefs.ui
/usr/share/rhythmbox/plugins/webremote/css/grids-responsive-min.css
/usr/share/rhythmbox/plugins/webremote/css/pure-min.css
/usr/share/rhythmbox/plugins/webremote/css/webremote.css
/usr/share/rhythmbox/plugins/webremote/js/webremote.js
/usr/share/rhythmbox/plugins/webremote/webremote-config.ui
/usr/share/rhythmbox/plugins/webremote/webremote.html
/usr/share/rhythmbox/rhythmbox.gep
/usr/share/vala/vapi/rb.vapi
/usr/share/vala/vapi/rhythmdb.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/rhythmbox/backends/rb-encoder.h
/usr/include/rhythmbox/backends/rb-player-gst-filter.h
/usr/include/rhythmbox/backends/rb-player-gst-helper.h
/usr/include/rhythmbox/backends/rb-player-gst-tee.h
/usr/include/rhythmbox/backends/rb-player.h
/usr/include/rhythmbox/lib/libmediaplayerid/mediaplayerid.h
/usr/include/rhythmbox/lib/rb-async-copy.h
/usr/include/rhythmbox/lib/rb-builder-helpers.h
/usr/include/rhythmbox/lib/rb-chunk-loader.h
/usr/include/rhythmbox/lib/rb-debug.h
/usr/include/rhythmbox/lib/rb-file-helpers.h
/usr/include/rhythmbox/lib/rb-gst-media-types.h
/usr/include/rhythmbox/lib/rb-list-model.h
/usr/include/rhythmbox/lib/rb-stock-icons.h
/usr/include/rhythmbox/lib/rb-string-value-map.h
/usr/include/rhythmbox/lib/rb-task-progress-simple.h
/usr/include/rhythmbox/lib/rb-task-progress.h
/usr/include/rhythmbox/lib/rb-util.h
/usr/include/rhythmbox/metadata/rb-ext-db-key.h
/usr/include/rhythmbox/metadata/rb-ext-db.h
/usr/include/rhythmbox/metadata/rb-metadata.h
/usr/include/rhythmbox/plugins/rb-plugin-macros.h
/usr/include/rhythmbox/podcast/rb-podcast-manager.h
/usr/include/rhythmbox/podcast/rb-podcast-parse.h
/usr/include/rhythmbox/podcast/rb-podcast-search.h
/usr/include/rhythmbox/rhythmdb/rb-refstring.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-entry-type.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-entry.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-import-job.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-property-model.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-query-model.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-query-result-list.h
/usr/include/rhythmbox/rhythmdb/rhythmdb-query-results.h
/usr/include/rhythmbox/rhythmdb/rhythmdb.h
/usr/include/rhythmbox/shell/rb-application.h
/usr/include/rhythmbox/shell/rb-history.h
/usr/include/rhythmbox/shell/rb-play-order.h
/usr/include/rhythmbox/shell/rb-playlist-manager.h
/usr/include/rhythmbox/shell/rb-removable-media-manager.h
/usr/include/rhythmbox/shell/rb-shell-player.h
/usr/include/rhythmbox/shell/rb-shell-preferences.h
/usr/include/rhythmbox/shell/rb-shell.h
/usr/include/rhythmbox/shell/rb-task-list.h
/usr/include/rhythmbox/shell/rb-track-transfer-batch.h
/usr/include/rhythmbox/shell/rb-track-transfer-queue.h
/usr/include/rhythmbox/sources/rb-auto-playlist-source.h
/usr/include/rhythmbox/sources/rb-browser-source.h
/usr/include/rhythmbox/sources/rb-device-source.h
/usr/include/rhythmbox/sources/rb-display-page-group.h
/usr/include/rhythmbox/sources/rb-display-page-model.h
/usr/include/rhythmbox/sources/rb-display-page-tree.h
/usr/include/rhythmbox/sources/rb-display-page.h
/usr/include/rhythmbox/sources/rb-media-player-source.h
/usr/include/rhythmbox/sources/rb-playlist-source.h
/usr/include/rhythmbox/sources/rb-playlist-xml.h
/usr/include/rhythmbox/sources/rb-source-search-basic.h
/usr/include/rhythmbox/sources/rb-source-search.h
/usr/include/rhythmbox/sources/rb-source.h
/usr/include/rhythmbox/sources/rb-static-playlist-source.h
/usr/include/rhythmbox/sources/rb-streaming-source.h
/usr/include/rhythmbox/sources/rb-transfer-target.h
/usr/include/rhythmbox/widgets/rb-button-bar.h
/usr/include/rhythmbox/widgets/rb-cell-renderer-pixbuf.h
/usr/include/rhythmbox/widgets/rb-cell-renderer-rating.h
/usr/include/rhythmbox/widgets/rb-dialog.h
/usr/include/rhythmbox/widgets/rb-entry-view.h
/usr/include/rhythmbox/widgets/rb-fading-image.h
/usr/include/rhythmbox/widgets/rb-library-browser.h
/usr/include/rhythmbox/widgets/rb-property-view.h
/usr/include/rhythmbox/widgets/rb-rating.h
/usr/include/rhythmbox/widgets/rb-search-entry.h
/usr/include/rhythmbox/widgets/rb-segmented-bar.h
/usr/include/rhythmbox/widgets/rb-song-info.h
/usr/include/rhythmbox/widgets/rb-source-toolbar.h
/usr/include/rhythmbox/widgets/rb-uri-dialog.h
/usr/lib64/librhythmbox-core.so
/usr/lib64/pkgconfig/rhythmbox.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/C/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/C/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/C/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/C/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/C/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/C/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/C/rhythmbox/figures/rb-window.png
/usr/share/help/C/rhythmbox/index.docbook
/usr/share/help/C/rhythmbox/legal.xml
/usr/share/help/ca/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/ca/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/ca/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/ca/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/ca/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/ca/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/ca/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/ca/rhythmbox/figures/rb-window.png
/usr/share/help/ca/rhythmbox/index.docbook
/usr/share/help/ca/rhythmbox/legal.xml
/usr/share/help/cs/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/cs/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/cs/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/cs/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/cs/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/cs/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/cs/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/cs/rhythmbox/figures/rb-window.png
/usr/share/help/cs/rhythmbox/index.docbook
/usr/share/help/cs/rhythmbox/legal.xml
/usr/share/help/da/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/da/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/da/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/da/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/da/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/da/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/da/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/da/rhythmbox/figures/rb-window.png
/usr/share/help/da/rhythmbox/index.docbook
/usr/share/help/da/rhythmbox/legal.xml
/usr/share/help/de/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/de/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/de/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/de/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/de/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/de/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/de/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/de/rhythmbox/figures/rb-window.png
/usr/share/help/de/rhythmbox/index.docbook
/usr/share/help/de/rhythmbox/legal.xml
/usr/share/help/el/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/el/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/el/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/el/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/el/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/el/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/el/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/el/rhythmbox/figures/rb-window.png
/usr/share/help/el/rhythmbox/index.docbook
/usr/share/help/el/rhythmbox/legal.xml
/usr/share/help/es/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/es/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/es/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/es/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/es/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/es/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/es/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/es/rhythmbox/figures/rb-window.png
/usr/share/help/es/rhythmbox/index.docbook
/usr/share/help/es/rhythmbox/legal.xml
/usr/share/help/eu/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/eu/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/eu/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/eu/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/eu/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/eu/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/eu/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/eu/rhythmbox/figures/rb-window.png
/usr/share/help/eu/rhythmbox/index.docbook
/usr/share/help/eu/rhythmbox/legal.xml
/usr/share/help/fr/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/fr/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/fr/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/fr/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/fr/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/fr/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/fr/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/fr/rhythmbox/figures/rb-window.png
/usr/share/help/fr/rhythmbox/index.docbook
/usr/share/help/fr/rhythmbox/legal.xml
/usr/share/help/gl/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/gl/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/gl/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/gl/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/gl/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/gl/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/gl/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/gl/rhythmbox/figures/rb-window.png
/usr/share/help/gl/rhythmbox/index.docbook
/usr/share/help/gl/rhythmbox/legal.xml
/usr/share/help/id/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/id/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/id/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/id/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/id/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/id/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/id/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/id/rhythmbox/figures/rb-window.png
/usr/share/help/id/rhythmbox/index.docbook
/usr/share/help/id/rhythmbox/legal.xml
/usr/share/help/it/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/it/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/it/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/it/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/it/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/it/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/it/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/it/rhythmbox/figures/rb-window.png
/usr/share/help/it/rhythmbox/index.docbook
/usr/share/help/it/rhythmbox/legal.xml
/usr/share/help/ja/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/ja/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/ja/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/ja/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/ja/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/ja/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/ja/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/ja/rhythmbox/figures/rb-window.png
/usr/share/help/ja/rhythmbox/index.docbook
/usr/share/help/ja/rhythmbox/legal.xml
/usr/share/help/oc/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/oc/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/oc/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/oc/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/oc/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/oc/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/oc/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/oc/rhythmbox/figures/rb-window.png
/usr/share/help/oc/rhythmbox/index.docbook
/usr/share/help/oc/rhythmbox/legal.xml
/usr/share/help/pt/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/pt/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/pt/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/pt/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/pt/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/pt/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/pt/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/pt/rhythmbox/figures/rb-window.png
/usr/share/help/pt/rhythmbox/index.docbook
/usr/share/help/pt/rhythmbox/legal.xml
/usr/share/help/pt_BR/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/pt_BR/rhythmbox/figures/rb-window.png
/usr/share/help/pt_BR/rhythmbox/index.docbook
/usr/share/help/pt_BR/rhythmbox/legal.xml
/usr/share/help/ro/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/ro/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/ro/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/ro/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/ro/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/ro/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/ro/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/ro/rhythmbox/figures/rb-window.png
/usr/share/help/ro/rhythmbox/index.docbook
/usr/share/help/ro/rhythmbox/legal.xml
/usr/share/help/ru/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/ru/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/ru/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/ru/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/ru/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/ru/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/ru/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/ru/rhythmbox/figures/rb-window.png
/usr/share/help/ru/rhythmbox/index.docbook
/usr/share/help/ru/rhythmbox/legal.xml
/usr/share/help/sl/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/sl/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/sl/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/sl/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/sl/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/sl/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/sl/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/sl/rhythmbox/figures/rb-window.png
/usr/share/help/sl/rhythmbox/index.docbook
/usr/share/help/sl/rhythmbox/legal.xml
/usr/share/help/sv/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/sv/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/sv/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/sv/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/sv/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/sv/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/sv/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/sv/rhythmbox/figures/rb-window.png
/usr/share/help/sv/rhythmbox/index.docbook
/usr/share/help/sv/rhythmbox/legal.xml
/usr/share/help/uk/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/uk/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/uk/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/uk/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/uk/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/uk/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/uk/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/uk/rhythmbox/figures/rb-window.png
/usr/share/help/uk/rhythmbox/index.docbook
/usr/share/help/uk/rhythmbox/legal.xml
/usr/share/help/zh_CN/rhythmbox/figures/rb-iradio-main.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-notification-zone.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-podcast-main.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-toolbar-prevplaynext.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-toolbar-repeat.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-toolbar-shuffle.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-volume-changer.png
/usr/share/help/zh_CN/rhythmbox/figures/rb-window.png
/usr/share/help/zh_CN/rhythmbox/index.docbook
/usr/share/help/zh_CN/rhythmbox/legal.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/librhythmbox-core.so.10
/usr/lib64/librhythmbox-core.so.10.0.0
/usr/lib64/rhythmbox/plugins/android/libandroid.so
/usr/lib64/rhythmbox/plugins/audiocd/libaudiocd.so
/usr/lib64/rhythmbox/plugins/audioscrobbler/libaudioscrobbler.so
/usr/lib64/rhythmbox/plugins/dbus-media-server/libdbus-media-server.so
/usr/lib64/rhythmbox/plugins/fmradio/libfmradio.so
/usr/lib64/rhythmbox/plugins/generic-player/libgeneric-player.so
/usr/lib64/rhythmbox/plugins/grilo/libgrilo.so
/usr/lib64/rhythmbox/plugins/iradio/libiradio.so
/usr/lib64/rhythmbox/plugins/mpris/libmpris.so
/usr/lib64/rhythmbox/plugins/mtpdevice/libmtpdevice.so
/usr/lib64/rhythmbox/plugins/notification/libnotification.so
/usr/lib64/rhythmbox/plugins/power-manager/libpower-manager.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/rhythmbox-metadata

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rhythmbox/3f772bdc589b117aeeb6fbbf5bd277d7c3015a56

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rhythmbox-client.1
/usr/share/man/man1/rhythmbox.1

%files locales -f rhythmbox.lang
%defattr(-,root,root,-)

