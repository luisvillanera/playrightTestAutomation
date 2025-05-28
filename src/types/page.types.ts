export interface IBasePage {
  navigate(): Promise<void>;
}

export interface ILoginPage extends IBasePage {
  login(username: string, password: string): Promise<void>;
  isSuccessMessageVisible(): Promise<boolean>;
  isErrorMessageVisible(): Promise<boolean>;
  getErrorMessage(): Promise<string>;
} 