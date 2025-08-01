import { render, screen } from '@testing-library/react';
import App from './App.jsx';

jest.mock('react-router-dom', () => ({
  BrowserRouter: ({ children }) => <div>{children}</div>,
  Routes: ({ children }) => <div>{children}</div>,
  Route: ({ element }) => <>{element}</>,
  useLocation: () => ({ pathname: '/' }),
  NavLink: ({ children }) => <div>{children}</div>,
  Link: ({ children }) => <div>{children}</div>,
}), { virtual: true });

test('renders main heading', () => {
  render(<App />);
  const headings = screen.getAllByRole('heading', { level: 1 });
  expect(headings.length).toBeGreaterThan(0);
});
