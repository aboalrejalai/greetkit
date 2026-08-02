Write-Output "Verifying project state..."

# Node.js
if (Test-Path "package.json") {
    Write-Output "Node.js project detected."
    if (Select-String -Path "package.json" -Pattern '"build"\s*:') {
        Write-Output "Running npm run build..."
        npm run build
    }
    if (Select-String -Path "package.json" -Pattern '"test"\s*:') {
        Write-Output "Running npm test..."
        npm test
    }
}

# Python
elseif (Test-Path "requirements.txt" -or Test-Path "pyproject.toml") {
    Write-Output "Python project detected."
    if (Get-Command "pytest" -ErrorAction SilentlyContinue) {
        Write-Output "Running pytest..."
        pytest
    } else {
        Write-Output "pytest not found. Skipping tests."
    }
}

# PHP
elseif (Test-Path "composer.json") {
    Write-Output "PHP project detected."
    if (Test-Path "vendor/bin/phpunit") {
        Write-Output "Running phpunit..."
        ./vendor/bin/phpunit
    } else {
        Write-Output "phpunit not found. Skipping tests."
    }
}

else {
    Write-Output "No supported testing/build framework automatically detected."
}

Write-Output "Verification complete."
