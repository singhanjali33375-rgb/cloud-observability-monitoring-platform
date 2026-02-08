#!/bin/bash
kubectl apply -f kubernetes/
kubectl apply -f metrics/
kubectl apply -f logs/
kubectl apply -f tracing/
kubectl apply -f alerts/
