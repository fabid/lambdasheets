function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Lambda sheets')
      .addItem('Update', 'menuItem1')
      .addToUi();
}
function menuItem1() {
  SpreadsheetApp.getUi()
     .alert('Update in progress.');
  UrlFetchApp.fetch('[deployed_url]', {muteHttpExceptions: true});
}
