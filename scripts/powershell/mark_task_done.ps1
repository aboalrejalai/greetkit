param(
    [Parameter(Mandatory=$true)]
    [string]$TaskID,

    [Parameter(Mandatory=$true)]
    [string]$PlanPath
)

if (-not $TaskId -or -not $PlanPath) {
    throw "Usage: .\mark_task_done.ps1 -TaskID 'TASK-001' -PlanPath 'greetkit/plans/001-feature-name.md'"
}

if (-Not (Test-Path $PlanPath)) {
    Write-Error "Plan file not found: $PlanPath"
    exit 1
}

$content = Get-Content -Path $PlanPath -Raw
# Replace "- [ ] TASK_ID" with "- [x] TASK_ID" preserving any tags or text that follow it.
$regex = "(?i)(-\s+\[\s*\]\s*)($TaskID)"
$replacement = "- [x] `$2"

$newContent = [regex]::Replace($content, $regex, $replacement)

if ($content -eq $newContent) {
    Write-Warning "Task '$TaskID' not found or already marked as done in $PlanPath"
} else {
    Set-Content -Path $PlanPath -Value $newContent -NoNewline -Encoding UTF8
    Write-Output "Successfully marked '$TaskID' as complete in $PlanPath"
}
