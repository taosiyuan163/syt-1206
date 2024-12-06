import { showNotify } from 'vant/es/notify'

export function useNotification() {
  const showSuccess = (message) => {
    showNotify({ type: 'success', message })
  }

  const showError = (message) => {
    showNotify({ type: 'danger', message })
  }

  const showWarning = (message) => {
    showNotify({ type: 'warning', message })
  }

  return {
    showSuccess,
    showError,
    showWarning
  }
}