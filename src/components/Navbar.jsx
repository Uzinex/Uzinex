import { useTranslation } from 'react-i18next';
import { NavLink, Link } from 'react-router-dom';
import LanguageSwitcher from '../LanguageSwitcher';
import '../styles/Navbar.css';

const Navbar = () => {
  const { t } = useTranslation();

  return (
    <header className="navbar">
      <div className="navbar-left">
        <Link to="/" className="logo">Uzinex</Link>
      </div>
      <nav className="navbar-right">
        <NavLink to="/about" className={({ isActive }) => isActive ? 'active' : ''}>{t('navbar.about')}</NavLink>
        <NavLink to="/projects" className={({ isActive }) => isActive ? 'active' : ''}>{t('navbar.projects')}</NavLink>
        <NavLink to="/contact" className={({ isActive }) => isActive ? 'active' : ''}>{t('navbar.contact')}</NavLink>
        <LanguageSwitcher />
      </nav>
    </header>
  );
};

export default Navbar;
