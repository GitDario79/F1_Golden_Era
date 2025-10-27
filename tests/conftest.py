# Ensure repo root is on sys.path in CI and locally
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
