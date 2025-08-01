import { useTranslation } from 'react-i18next';
import LanguageSwitcher from './LanguageSwitcher';
import './Navbar.css';

const Navbar = () => {
  const { t } = useTranslation();

  return (
    <header className="navbar">
      <div className="navbar-left">
        <span className="logo">Uzinex</span>
      </div>
      <nav className="navbar-right">
        <a href="#about">{t('navbar.about')}</a>
        <a href="#projects">{t('navbar.projects')}</a>
        <a href="#contact">{t('navbar.contact')}</a>
        <LanguageSwitcher />
      </nav>
    </header>
  );
};

export default Navbar;
