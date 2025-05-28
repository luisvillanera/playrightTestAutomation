export const LoginLocators = {
  inputs: {
    username: '#username',
    password: '#password'
  },
  buttons: {
    submit: '#submit'
  },
  messages: {
    success: '.has-text-align-center',
    error: '#error'
  }
} as const;

export type LoginLocatorKeys = typeof LoginLocators; 