#!/usr/bin/env bash

echo "Verifying project state..."

# Node.js
if [ -f "package.json" ]; then
    echo "Node.js project detected."
    if grep -q '"build"\s*:' package.json; then
        echo "Running npm run build..."
        npm run build
    fi
    if grep -q '"test"\s*:' package.json; then
        echo "Running npm test..."
        npm test
    fi

# Python
elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    echo "Python project detected."
    if command -v pytest &>/dev/null; then
        echo "Running pytest..."
        pytest
    else
        echo "pytest not found. Skipping tests."
    fi

# PHP
elif [ -f "composer.json" ]; then
    echo "PHP project detected."
    if [ -f "vendor/bin/phpunit" ]; then
        echo "Running phpunit..."
        ./vendor/bin/phpunit
    else
        echo "phpunit not found. Skipping tests."
    fi

else
    echo "No supported testing/build framework automatically detected."
fi

echo "Verification complete."
