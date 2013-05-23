function checkURLs() {
  var errors = [];
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var rows = ss.getDataRange().getValues();
  for (i in rows) {
    var url = rows[i][0];
    var response = UrlFetchApp.fetch(url, {muteHttpExceptions: true});
    var status = response.getResponseCode();
    if (status !== 200)
      errors.push(status + ' - '+ url);
  }
  if (errors.length) {
    var emailTo = Session.getActiveUser().getEmail();
    MailApp.sendEmail(emailTo, 'Sitemonitor Status', errors.join('\n'));
  }
}