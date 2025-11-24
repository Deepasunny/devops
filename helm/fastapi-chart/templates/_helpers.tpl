{{- define "fastapi-chart.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "fastapi-chart.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}

{{- define "fastapi-chart.labels" -}}
app.kubernetes.io/name: {{ include "fastapi-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
