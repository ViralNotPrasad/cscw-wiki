/*global jQuery, mediaWiki, insertTags*/
(function ($, mw) {
  'use strict';
  var wgNamespaceNumber = mw.config.get('wgNamespaceNumber'),
    wgAction = mw.config.get('wgAction'),
    wgTitle = mw.config.get('wgTitle');
  if (!((wgNamespaceNumber % 2 || wgNamespaceNumber === 4) && (wgAction === 'edit' || wgAction === 'submit'))) {
    return;
  }
  $(function () {
    var copywarn = $('#editpage-copywarn'), wpSave = $('#wpSave'), signLink;
    if (copywarn.length === 0 || wpSave.length === 0) {
      return;
    }
    // avoid warning on project pages blacklist
    if (mw.config.get('wgNamespaceNumber') === 4 && !mw.config.get('wgTitle').match('^(سوالات|معاونت برائے صارفین|دیوان عام|اطلاع|چائے خانہ)')) {
      return;
    }
    if (mw.config.get('wgNamespaceNumber') === 4 && mw.config.get('wgTitle').match('^(درخواست)')) {
      return;
    }
    // Not to add sign request in WP:DAR and request for bots
    if (wgTitle.match('(درخواست تخلیق)')){
    	return;
    }
    window.warningDone = false;
    signLink = $('<a>', { href: '#', html: '~~' + '~~' }).click(function (e) {
      e.preventDefault();
      insertTags(' ~~' + '~~', '', '');
    });
    copywarn
      .html('براہ کرم تبادلۂ خیال صفحات میں اپنی دستخط درج کریں ')
      .append(signLink)
      .css({
        padding: '2px',
        background: '#F7F7F7',
        border: '1px solid gray'
      });
    wpSave.click(function (e) {
      if (window.warningDone || $('#wpTextbox1').val().indexOf('~~' + '~~') !== -1) { return; }
      e.preventDefault();
      window.warningDone = true;
      copywarn
        .html('')
        .append(
          'براہ کرم پیغام کے آخر میں اپنی دستخط  ',
          signLink,
          ' درج کریں (',
          $('<a href="/wiki/ویکیپیڈیا:دستخط" title="(ربط نئے صفحے میں کھلے گا)" target=_blank>مزید تفصیلات↗</a>'), //→ ↗
          ')'
        )
        .css({
          background: '#FFD080',
          border: '1px solid orange'
        });
    });
  });
}(jQuery, mediaWiki));