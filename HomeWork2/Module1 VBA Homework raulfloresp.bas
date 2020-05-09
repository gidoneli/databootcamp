Attribute VB_Name = "Module1"
Option Explicit

Dim ws As Worksheet


Sub StockAnalysis()

' Loop to repite an action on all Excel sheets in the Active Woorkbook
' Reference used: https://powerspreadsheets.com/excel-vba-sheets-worksheets/

Dim LastRow As Long

For Each ws In ActiveWorkbook.Worksheets
    ws.Activate
        
    'Read and get the last row in the worksheet
    'Multiple ways to get the last row but I used the one with the less coding
    ' https://www.wallstreetmojo.com/vba-last-row/
    
    LastRow = Cells(Rows.Count, "A").End(xlUp).Row
    Range("H1").Value = LastRow
    
    ' I tried an other alternative to extract unique values on a range but I was not able to solve a loop issue_
    ' so I abondened it
    'https://www.listendata.com/2013/05/excel-3-ways-to-extract-unique-values.html
    
    '    ActiveSheet.Range("B2:B" & lastrow).AdvancedFilter _
    '    Action:=xlFilterCopy, _
    '    CopyToRange:=ActiveSheet.Range("D2"), _
    '    Unique:=True
    
    
    ' Define general variables
    Dim Ticker As String
    Dim Yearly_Change As Double
    Dim Opening_Price As Double
    Dim Closing_Price As Double
    Dim Percent_Change As Double
    Dim Volume As Double
    Dim i As Double
    Dim j As Double
    Dim k As Double
    Dim Row As Integer
    Dim YearlyLastRow As Integer
        
    
    'Assign Titles to our new columns
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"
    
    ' Set initial values and initial calculations outside the loop
    Row = 2
    Opening_Price = Cells(2, 3).Value

    
    For i = 2 To LastRow
        
        ' Validate the Ticker value and check vs initial value
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
    
            ' Read and Add the Ticker Name
            Ticker = Cells(i, 1).Value
            Cells(Row, 9).Value = Ticker
        
            ' Add Closing Price
            Closing_Price = Cells(i, 6).Value
        
            ' Calculate and Add Yearly Change
            Yearly_Change = Closing_Price - Opening_Price
            Cells(Row, 10).Value = Yearly_Change
    
        ' Calculate and Add Percent Change
        If (Opening_Price = 0 And Closing_Price = 0) Then
        Percent_Change = 0
        
            ElseIf (Opening_Price = 0 And Closing_Price <> 0) Then
            Percent_Change = 1
            
            Else
            Percent_Change = Yearly_Change / Opening_Price
            Cells(Row, 11).Value = Percent_Change
            Cells(Row, 11).NumberFormat = "0.00%"
    
        End If
        
            ' Calculate and Add Total Volume
            Volume = Volume + Cells(i, 7).Value
            Cells(Row, 12).Value = Volume
        
            ' Update and Add one to the summary table row
            Row = Row + 1
        
            ' reset the Open Price
            Opening_Price = Cells(i + 1, 3)
        
            ' reset the Volumn Total
            Volume = 0
        
            'if cells are the same ticker
    
        Else
            Volume = Volume + Cells(i, 7).Value
        End If
    
    Next i

    'Determine the Last Row of Yearly Change per WS
    YearlyLastRow = ws.Cells(Rows.Count, 10).End(xlUp).Row
    
    ' conditional formatting that will highlight positive change in green and negative change in red
    For j = 2 To YearlyLastRow
        If (Cells(j, 10).Value >= 0) Then
            Cells(j, 10).Interior.ColorIndex = 4
        ElseIf Cells(j, 10).Value < 0 Then
            Cells(j, 10).Interior.ColorIndex = 3
        End If
    
    Next j


'Your solution will also be able to return the stock with the “Greatest % increase”, _
'_“Greatest % decrease” and “Greatest total volume”.


' Set cell names for Greatest % increase”, Greatest % decrease and Greatest total volume
Cells(2, 15).Value = "Greatest % Increase"
Cells(3, 15).Value = "Greatest % Decrease"
Cells(4, 15).Value = "Greatest Total Volume"
Cells(1, 16).Value = "Ticker"
Cells(1, 17).Value = "Stock Value"

' Loop trough tickers to find the greatest increase, descrease, and volume, and associated tickers
' Reference of coding method:
' https://docs.microsoft.com/en-us/office/vba/api/Excel.WorksheetFunction

For k = 2 To YearlyLastRow
    If Cells(k, 11).Value = Application.WorksheetFunction.Max(ws.Range("K2:K" & YearlyLastRow)) Then
        Cells(2, 16).Value = Cells(k, 9).Value
        Cells(2, 17).Value = Cells(k, 11).Value
        Cells(2, 17).NumberFormat = "0.00%"
    ElseIf Cells(k, 11).Value = Application.WorksheetFunction.Min(ws.Range("K2:K" & YearlyLastRow)) Then
        Cells(3, 16).Value = Cells(k, 9).Value
        Cells(3, 17).Value = Cells(k, 11).Value
        Cells(3, 17).NumberFormat = "0.00%"
    ElseIf Cells(k, 12).Value = Application.WorksheetFunction.Max(ws.Range("L2:L" & YearlyLastRow)) Then
        Cells(4, 16).Value = Cells(k, 9).Value
        Cells(4, 17).Value = Cells(k, 12).Value
    End If
Next k


Next ws

End Sub


